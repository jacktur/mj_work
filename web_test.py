# app.py - 重构后的Flask应用
from flask import Flask, request, render_template_string, session, redirect, url_for,jsonify
from functools import wraps
from datetime import timedelta

from pymysql.connections import DEFAULT_USER

from db_ops import get_conn
# 导入数据库操作函数
from 敏捷.敏捷管理2.db_ops import (
    user_get,
    verify_password,
    user_exists,
    user_save,
    user_name_change
)

# 导入注册相关函数
from 敏捷.敏捷管理2.registration_only2 import (
    start_registration,
    finsh_registration
)

# 导入模板
from templates import LOGIN_PAGE, REGISTER_PAGE, INDEX_PAGE

# ==================== Flask 应用配置 ====================
app = Flask(__name__)
app.secret_key = "dev-123"
app.permanent_session_lifetime = timedelta(minutes=30)


# ==================== 装饰器 ====================
def login_required(f):
    """登录验证装饰器"""

    @wraps(f)
    def wrapped(*args, **kwargs):
        if "email" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)

    return wrapped


# ==================== 路由：根路径 ====================
@app.route("/")
def root():
    """根路径重定向到登录页"""
    return redirect(url_for("login"))


# ==================== 路由：登录 ====================
@app.route("/login", methods=["GET", "POST"])
def login():
    """登录页面和登录处理"""
    # GET: 显示登录表单
    if request.method == "GET":
        return render_template_string(LOGIN_PAGE)

    # POST: 处理登录或跳转注册
    action = request.form.get("action")

    # 用户点击了"注册"按钮 - 直接跳转,不验证表单
    if action == "register":
        return redirect(url_for("register"))

    # 用户点击了"登录"按钮 - 验证表单
    if action == "login":
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "").strip()

        # 验证输入
        if not email or not password:
            return render_template_string(
                LOGIN_PAGE,
                error="邮箱和密码不能为空"
            )

        # 获取用户信息
        user = user_get(email)

        if not user:
            return render_template_string(LOGIN_PAGE, error="账号不存在,请先注册")

        if not user:
            return render_template_string(
                LOGIN_PAGE,
                error="账号不存在,请先注册"
            )

        # 验证密码
        password_valid = verify_password(
            password,
            user["password_hash"],
            user["salt"],
            user["iterations"]
        )

        if not password_valid:
            return render_template_string(
                LOGIN_PAGE,
                error="密码错误"
            )

        # 登录成功,设置 session
        session['user_id']=user['id']
        session["email"] = user["Email"]
        session["users_name"] = user["Users_name"]
        # ... 验证逻辑 ...
        session['show_welcome'] = True

        return redirect(url_for("index"))

    # 未知操作
    return redirect(url_for("login"))


# ==================== 路由：注册 ====================
@app.route("/register", methods=["GET", "POST"])
def register():
    """注册页面和注册处理"""
    # GET: 显示注册表单
    if request.method == "GET":
        return render_template_string(
            REGISTER_PAGE,
            email="",
            message=""
        )

    # POST: 处理注册或发送验证码
    action = request.form.get("action")
    email = request.form.get("email", "").strip()
    password = request.form.get("password", "").strip()
    code = request.form.get("code", "").strip()

    # 处理发送验证码
    if action == "send_code":
        ok, msg = start_registration(email, ttl=300)
        return render_template_string(
            REGISTER_PAGE,
            email=email,
            password=password,
            message=msg
        )

    # 处理注册
    if action == "register":
        username = email.split("@")[0]
        ok, msg = finsh_registration(
            email,
            code,
            password,
            username,
            ttl=300
        )

        if not ok:
            return render_template_string(
                REGISTER_PAGE,
                email=email,
                message=msg
            )

        # 注册成功,跳转到登录页
        return redirect(url_for("login"))

    # 未知操作
    return render_template_string(
        REGISTER_PAGE,
        email=email,
        message="无效的操作"
    )


# ==================== 路由：首页 ====================
@app.route("/index")
@login_required
def index():
    """用户首页(需要登录)"""
    show_welcome = session.pop('show_welcome', False)  # 👈 添加这一行，获取并清除标记
    return render_template_string(INDEX_PAGE, show_welcome=show_welcome)

# ==================== 创建任务 ====================
@app.route("/api/tasks",methods=['POST'])
@login_required
def task_create():
    user_id=session['user_id']
    data=request.get_json()
    title=data.get('title')
    priority=data.get('priority')
    description=data.get('description','')
    due_date = data.get('due_date')
    if not title:
        return jsonify({'error':'标题不能为空'}),400 #请求错误

    with get_conn() as conn, conn.cursor() as cur:

        cur.execute(
            "insert into tasks (user_id,title,description,priority,due_date,status) values (%s,%s,%s,%s,%s,'pending') ",
            (user_id, title,description,priority,due_date,)
        )
        task_id=cur.lastrowid
        conn.commit()
        return jsonify(
            {
                'success': True,
                "task_id": task_id,
                "title": title,
                'priority': priority,
                'description': description,
                'due_date': due_date,
            }
        ),201 # ← HTTP 状态码 201 表示创建成功


# =================== 切换任务状态 ====================
@app.route("/api/tasks/<int:task_id>/toggle", methods=["POST"])
@login_required
def task_toggle(task_id):
    user_id = session['user_id']

    with get_conn() as conn, conn.cursor() as cur:
        # 验证权限
        cur.execute(
            'SELECT status FROM tasks WHERE task_id=%s AND user_id=%s',
            (task_id, user_id)
        )
        task = cur.fetchone()

        if not task:
            return jsonify({'error': '任务不存在'}), 404

        # 切换状态
        current_status = task['status']
        new_status = 'completed' if current_status == 'pending' else 'pending'

        # 更新状态和完成时间
        if new_status == 'completed':
            cur.execute(
                'UPDATE tasks SET status=%s, completed_at=NOW() WHERE task_id=%s',
                (new_status, task_id)
            )
        else:
            cur.execute(
                'UPDATE tasks SET status=%s, completed_at=NULL WHERE task_id=%s',
                (new_status, task_id)
            )

        return jsonify({
            'success': True,
            'new_status': new_status
        }), 200


# =================== 查询任务 ====================
@app.route("/api/tasks",methods=['GET'])
@login_required
def task_list():
    user_id=session['user_id']

    with get_conn() as conn, conn.cursor() as cur:
        cur.execute(
            'SELECT task_id, title, description, status, priority,due_date, created_at FROM tasks WHERE user_id=%s ORDER BY created_at DESC',
            (user_id,)
        )

        tasks=cur.fetchall()
        return jsonify(
            {
                'success': True,
                "tasks": tasks,
            }
        ),200





# =================== 更新任务-编辑任务 ====================
@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
@login_required
def update_task(task_id):
    user_id = session['user_id']
    data = request.get_json()  #
    title = data.get('title')  #
    priority = data.get('priority', 'medium')  #
    description = data.get('description', '')
    due_date = data.get('due_date')


    if not title:
        return jsonify({'success': False, 'error': '任务标题不能为空'}), 400

    try:
        with get_conn() as conn:
            with conn.cursor() as cur:
                # 检查任务是否属于当前用户
                cur.execute(
                    "SELECT user_id FROM tasks WHERE task_id = %s",
                    (task_id,)
                )
                task = cur.fetchone()

                if not task:
                    return jsonify({'success': False, 'error': '任务不存在'}), 404

                if task['user_id'] != user_id:
                    return jsonify({'success': False, 'error': '无权限修改此任务'}), 403

                # 更新任务
                cur.execute(
                    "UPDATE tasks SET title = %s, priority = %s,description=%s,due_date = %s WHERE task_id = %s",
                    (title, priority, description,due_date,task_id)
                )
                conn.commit()

                return jsonify({'success': True}), 200

    except Exception as e:
        print(f"错误: {str(e)}")
        return jsonify({'success': False, 'error': '服务器错误'}), 500


# =================== 删除任务 ====================
@app.route("/api/tasks/<int:task_id>", methods=["DELETE"])
@login_required
def task_delete(task_id):
    user_id=session['user_id']
    with get_conn() as conn, conn.cursor() as cur:
        #验证权限
        cur.execute(
            'select * from tasks where task_id=%s AND user_id=%s',(task_id,user_id,)
        )
        task=cur.fetchone()
        if not task:
            return jsonify(
                {'error':'数据错误'}
            ),404

        cur.execute(
            'delete from tasks where task_id=%s',(task_id,)
        )
        conn.commit()

        return jsonify(
            {
                'success': True,
            }
        ),200





# ==================== 路由：修改用户名 ====================
@app.route("/change-name", methods=["POST"])
@login_required
def change_name():
    """修改用户名"""
    new_name = request.form.get("new_name", "").strip()

    # 验证输入
    if not new_name:
        return "名字不能为空", 400

    # 更新数据库
    ok = user_name_change(session["email"], new_name)

    if not ok:
        return "修改失败", 500

    # 更新 session
    session["users_name"] = new_name

    return redirect(url_for("index"))


# ==================== 路由:退出登录 ====================
@app.route("/logout")
def logout():
    """退出登录"""
    session.pop("user_id", None)
    session.pop("email", None)
    session.pop("users_name", None)
    session.pop("show_welcome", False)
    return redirect(url_for("login"))


# ==================== 启动应用 ====================
if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )