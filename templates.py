# templates.py - HTML 模板定义

# ==================== 登录页面模板 ====================
LOGIN_PAGE = """
<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <title>登录</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            background: url("/static/bg.jpg") no-repeat center center fixed;
            background-size: cover;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Arial, sans-serif;
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .card {
            background: rgba(255, 255, 255, 0.75);
            width: 360px;
            border-radius: 16px;
            padding: 28px;
            box-shadow: 0 12px 30px rgba(15, 23, 42, 0.12);
            margin-top: -60px;
        }

        h1 {
            margin-top: 0;
            font-size: 22px;
            text-align: center;
            margin-bottom: 20px;
        }

        /* 浮动标签输入框 */
        .auth-field {
            position: relative;
            margin-bottom: 18px;
        }

        .auth-field .input {
            font-size: 16px;
            padding: 10px 10px 10px 5px;
            display: block;
            width: 100%;
            border: none;
            border-bottom: 1px solid #515151;
            background: transparent;
        }

        .auth-field .input:focus {
            outline: none;
        }

        .auth-field label {
            color: #999;
            font-size: 18px;
            font-weight: normal;
            position: absolute;
            pointer-events: none;
            left: 5px;
            top: 10px;
            transition: 0.2s ease all;
        }

        .auth-field .input:focus ~ label,
        .auth-field .input:valid ~ label {
            top: -20px;
            font-size: 14px;
            color: #5264AE;
        }

        .auth-field .bar {
            position: relative;
            display: block;
            width: 100%;
        }

        .auth-field .bar:before,
        .auth-field .bar:after {
            content: '';
            height: 2px;
            width: 0;
            bottom: 1px;
            position: absolute;
            background: #5264AE;
            transition: 0.2s ease all;
        }

        .auth-field .bar:before { left: 50%; }
        .auth-field .bar:after { right: 50%; }

        .auth-field .input:focus ~ .bar:before,
        .auth-field .input:focus ~ .bar:after {
            width: 50%;
        }

        .auth-field .highlight {
            position: absolute;
            height: 60%;
            width: 100px;
            top: 25%;
            left: 0;
            pointer-events: none;
            opacity: 0.5;
        }

        .auth-field .input:focus ~ .highlight {
            animation: inputHighlighter 0.3s ease;
        }

        @keyframes inputHighlighter {
            from { background: #5264AE; }
            to { width: 0; background: transparent; }
        }

        /* 按钮样式 */
        .register_and_login {
            display: flex;
            gap: 12px;
            margin-top: 16px;
            justify-content: center;
        }

        button {
            width: 30%;
            background: #2563eb;
            color: #fff;
            border: none;
            padding: 10px 14px;
            border-radius: 10px;
            font-size: 15px;
            cursor: pointer;
        }

        button:hover {
            background: #1d4ed8;
        }

        .muted {
            text-align: center;
            color: #94a3b8;
            font-size: 12px;
            margin-top: 14px;
        }

        .error {
            background: #fee;
            color: #c33;
            padding: 10px;
            border-radius: 8px;
            margin-bottom: 15px;
            text-align: center;
            font-size: 14px;
        }
    </style>
</head>

<body>
    <div class="card">
        <h1>登录</h1>

        {% if error %}
        <div class="error">{{ error }}</div>
        {% endif %}

        <form method="post">
            <div class="auth-field">
                <input type="email" name="email" class="input"  placeholder=" ">
                <span class="highlight"></span>
                <span class="bar"></span>
                <label>邮箱</label>
            </div>

            <div class="auth-field">
                <input type="password" name="password" class="input"  placeholder=" ">
                <span class="highlight"></span>
                <span class="bar"></span>
                <label>密码</label>
            </div>

            <div class="register_and_login">
                <button type="submit" name="action" value="login">登录</button>
                <button type="submit" name="action" value="register">注册</button>
            </div>
        </form>

        <div class="muted">请使用你已注册的邮箱登录</div>
    </div>
</body>
</html>
"""

# ==================== 注册页面模板 ====================
REGISTER_PAGE = """
<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <title>注册</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Arial, sans-serif;
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            background: url("/static/bg.jpg") no-repeat center center fixed;
            background-size: cover;
        }

        .card {
            background: rgba(255, 255, 255, 0.75);
            width: 360px;
            border-radius: 16px;
            padding: 24px;
            box-shadow: 0 12px 30px rgba(15, 23, 42, 0.12);
        }

        h2 {
            text-align: center;
            margin-top: 0;
        }

        /* 浮动标签输入框样式 */
        .auth-field {
            position: relative;
            margin-bottom: 18px;
        }

        .auth-field .input {
            font-size: 16px;
            padding: 10px 10px 10px 5px;
            display: block;
            width: 100%;
            border: none;
            border-bottom: 1px solid #515151;
            background: transparent;
        }

        .auth-field .input:focus {
            outline: none;
        }

        .auth-field label {
            color: #999;
            font-size: 18px;
            font-weight: normal;
            position: absolute;
            pointer-events: none;
            left: 5px;
            top: 10px;
            transition: 0.2s ease all;
        }

        .auth-field .input:focus ~ label,
        .auth-field .input:valid ~ label {
            top: -20px;
            font-size: 14px;
            color: #5264AE;
        }

        .auth-field .bar {
            position: relative;
            display: block;
            width: 100%;
        }

        .auth-field .bar:before,
        .auth-field .bar:after {
            content: '';
            height: 2px;
            width: 0;
            bottom: 1px;
            position: absolute;
            background: #5264AE;
            transition: 0.2s ease all;
        }

        .auth-field .bar:before { left: 50%; }
        .auth-field .bar:after { right: 50%; }

        .auth-field .input:focus ~ .bar:before,
        .auth-field .input:focus ~ .bar:after {
            width: 50%;
        }

        .auth-field .highlight {
            position: absolute;
            height: 60%;
            width: 100px;
            top: 25%;
            left: 0;
            pointer-events: none;
            opacity: 0.5;
        }

        .auth-field .input:focus ~ .highlight {
            animation: inputHighlighter 0.3s ease;
        }

        @keyframes inputHighlighter {
            from { background: #5264AE; }
            to { width: 0; background: transparent; }
        }

        /* 验证码字段特殊布局 */
        .code-field {
            position: relative;
        }

        .code-field .input {
            width: calc(100% - 160px);
        }

        .code-field .code-btn {
            position: absolute;
            right: 0;
            top: 6px;
            border: none;
            background: transparent;
            padding: 0;
            cursor: pointer;
        }

        .code-btn .shadow {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            border-radius: 12px;
            background: hsl(0deg 0% 0% / 0.25);
            transform: translateY(2px);
            transition: transform 600ms cubic-bezier(.3, .7, .4, 1);
        }

        .code-btn .edge {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            border-radius: 12px;
            background: linear-gradient(
                to left,
                hsl(201, 49%, 60%) 0%,
                hsl(204, 68%, 38%) 8%,
                hsl(209, 58%, 54%) 92%,
                hsl(199, 100%, 82%) 100%
            );
        }

        .code-btn .front {
            display: block;
            position: relative;
            padding: 12px 27px;
            border-radius: 12px;
            font-size: 1.1rem;
            color: white;
            background: hsl(215, 86%, 54%);
            transform: translateY(-4px);
            transition: transform 600ms cubic-bezier(.3, .7, .4, 1);
        }

        .code-btn:hover {
            filter: brightness(110%);
        }

        .code-btn:hover .front {
            transform: translateY(-6px);
            transition: transform 250ms cubic-bezier(.3, .7, .4, 1.5);
        }

        .code-btn:active .front {
            transform: translateY(-2px);
            transition: transform 34ms;
        }

        .code-btn:hover .shadow {
            transform: translateY(4px);
            transition: transform 250ms cubic-bezier(.3, .7, .4, 1.5);
        }

        .code-btn:active .shadow {
            transform: translateY(1px);
            transition: transform 34ms;
        }

        /* 注册按钮样式 */
        .Btn-Container {
            display: flex;
            width: 100%;
            height: 60px;
            background-color: #c97133;
            border-radius: 40px;
            box-shadow: 0px 5px 10px #bebebe;
            justify-content: space-between;
            align-items: center;
            border: none;
            cursor: pointer;
            margin-top: 20px;
        }

        .icon-Container {
            width: 45px;
            height: 45px;
            background-color: #edf5cf;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 50%;
            border: 3px solid #1d2129;
        }

        .text {
            width: calc(170px - 45px);
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 1.1em;
            letter-spacing: 1.2px;
        }

        .icon-Container svg {
            transition-duration: 1.5s;
        }

        .Btn-Container:hover .icon-Container svg {
            animation: arrow 1s linear infinite;
        }

        @keyframes arrow {
            0% { opacity: 0; margin-left: 0px; }
            100% { opacity: 1; margin-left: 10px; }
        }

        .msg {
            margin-top: 10px;
            font-size: 12px;
            color: #94a3b8;
            text-align: center;
        }
    </style>
</head>

<body>
    <div class="card">
        <h2>注册</h2>
        <form method="post">
            <!-- 邮箱输入 -->
            <div class="auth-field">
                <input required type="email" name="email" class="input" value="{{ email or '' }}" placeholder=" ">
                <span class="highlight"></span>
                <span class="bar"></span>
                <label>邮箱</label>
            </div>

            <!-- 密码输入 -->
            <div class="auth-field">
                <input required type="password" name="password" class="input" value="{{ password or '' }}" placeholder=" ">
                <span class="highlight"></span>
                <span class="bar"></span>
                <label>密码</label>
            </div>

            <!-- 验证码输入 -->
            <div class="auth-field code-field">
                <input type="text" name="code" class="input" placeholder=" ">
                <span class="highlight"></span>
                <span class="bar"></span>
                <label>验证码</label>

                <button type="submit" name="action" value="send_code" class="code-btn">
                    <span class="shadow"></span>
                    <span class="edge"></span>
                    <span class="front text">发送验证码</span>
                </button>
            </div>

            <!-- 注册按钮 -->
            <button type="submit" name="action" value="register" class="Btn-Container">
                <span class="text">let's go! 注册</span>
                <span class="icon-Container">
                    <svg width="16" height="19" viewBox="0 0 16 19" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <circle cx="1.61" cy="1.61" r="1.5" fill="black"></circle>
                        <circle cx="5.73" cy="1.61" r="1.5" fill="black"></circle>
                        <circle cx="5.73" cy="5.55" r="1.5" fill="black"></circle>
                        <circle cx="9.85" cy="5.55" r="1.5" fill="black"></circle>
                        <circle cx="9.85" cy="9.5" r="1.5" fill="black"></circle>
                        <circle cx="13.98" cy="9.5" r="1.5" fill="black"></circle>
                        <circle cx="5.73" cy="13.44" r="1.5" fill="black"></circle>
                        <circle cx="9.85" cy="13.44" r="1.5" fill="black"></circle>
                        <circle cx="1.61" cy="17.38" r="1.5" fill="black"></circle>
                        <circle cx="5.73" cy="17.38" r="1.5" fill="black"></circle>
                    </svg>
                </span>
            </button>
        </form>

        <div class="msg">{{ message or '' }}</div>
    </div>

    {% if message %}
    <script>
        alert("{{ message }}");
    </script>
    {% endif %}
</body>
</html>
"""

# ==================== 首页模板 ====================
INDEX_PAGE = """
<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Workspace Ultimate | 数据中心</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">

<style>
:root {
--bg-deep: #050507;
--bg-panel: rgba(20, 20, 25, 0.65);
--bg-panel-light: rgba(255, 255, 255, 0.03);
--neon-blue: #3b82f6;
--neon-purple: #8b5cf6;
--neon-pink: #ec4899;
--neon-green: #10b981;
--neon-orange: #f59e0b;
--neon-red: #ef4444;
--text-main: #ffffff;
--text-muted: #9ca3af;
--border: rgba(255, 255, 255, 0.08);
--glass: blur(16px);
--radius: 20px;
}

* { margin: 0; padding: 0; box-sizing: border-box; outline: none; }

body {
background-color: var(--bg-deep);
color: var(--text-main);
font-family: 'Space Grotesk', sans-serif;
height: 100vh;
overflow: hidden;
display: flex;
background-image: 
radial-gradient(circle at 10% 20%, rgba(59, 130, 246, 0.08), transparent 25%),
radial-gradient(circle at 90% 80%, rgba(236, 72, 153, 0.08), transparent 25%);
}

::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-thumb { background: #333; border-radius: 2px; }

@keyframes fadeIn {
from { opacity: 0; transform: translateY(20px); }
to { opacity: 1; transform: translateY(0); }
}

@keyframes slideIn {
from { opacity: 0; transform: translateX(-20px); }
to { opacity: 1; transform: translateX(0); }
}

@keyframes scaleIn {
from { opacity: 0; transform: scale(0.9); }
to { opacity: 1; transform: scale(1); }
}

@keyframes float {
0%, 100% { transform: translateY(0px); }
50% { transform: translateY(-10px); }
}

.sidebar {
width: 80px;
background: rgba(10, 10, 12, 0.8);
backdrop-filter: var(--glass);
border-right: 1px solid var(--border);
display: flex; flex-direction: column; align-items: center;
padding: 30px 0; z-index: 10;
}

.logo-box {
width: 48px; height: 48px;
background: linear-gradient(135deg, var(--neon-blue), var(--neon-purple));
border-radius: 12px; display: grid; place-items: center; margin-bottom: 40px;
box-shadow: 0 0 20px rgba(139, 92, 246, 0.3);
animation: float 3s ease-in-out infinite;
}

.nav-icon {
width: 48px; height: 48px; border-radius: 12px; margin-bottom: 16px;
display: grid; place-items: center; color: var(--text-muted);
cursor: pointer; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
position: relative;
}
.nav-icon:hover { 
background: rgba(255,255,255,0.05); 
color: white;
transform: translateX(5px);
}
.nav-icon.active { 
background: rgba(59, 130, 246, 0.15); 
color: var(--neon-blue);
transform: translateX(5px);
}
.nav-icon.active::after {
content: ''; position: absolute; left: 0; top: 50%; transform: translateY(-50%);
width: 3px; height: 20px; background: var(--neon-blue); border-radius: 0 4px 4px 0;
animation: slideIn 0.3s ease;
}

.main-container {
flex: 1; 
display: grid;
grid-template-columns: 1fr 320px;
grid-template-rows: auto 1fr;
gap: 20px;
padding: 20px;
overflow: hidden;
}

.top-stats-bar {
grid-column: 1 / -1;
display: grid;
grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
gap: 16px;
animation: fadeIn 0.5s ease;
}

.stat-card {
background: var(--bg-panel);
border: 1px solid var(--border);
border-radius: 16px;
padding: 20px;
backdrop-filter: var(--glass);
transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
position: relative;
overflow: hidden;
}

.stat-card::before {
content: '';
position: absolute;
top: 0; left: -100%;
width: 100%; height: 100%;
background: linear-gradient(90deg, transparent, rgba(255,255,255,0.05), transparent);
transition: left 0.5s;
}

.stat-card:hover::before {
left: 100%;
}

.stat-card:hover {
transform: translateY(-5px);
border-color: rgba(255,255,255,0.2);
box-shadow: 0 10px 30px rgba(0,0,0,0.3);
}

.stat-label {
font-size: 11px;
color: var(--text-muted);
text-transform: uppercase;
letter-spacing: 1px;
margin-bottom: 8px;
font-weight: 600;
}

.stat-value {
font-size: 32px;
font-weight: 700;
font-family: 'JetBrains Mono', monospace;
margin-bottom: 4px;
}

.stat-trend {
font-size: 12px;
color: var(--neon-green);
display: flex;
align-items: center;
gap: 4px;
}

.task-section {
display: flex;
flex-direction: column;
background: var(--bg-panel);
border: 1px solid var(--border);
border-radius: var(--radius);
backdrop-filter: var(--glass);
overflow: hidden;
animation: fadeIn 0.6s ease;
}

.control-panel {
display: flex;
flex-direction: column;
gap: 16px;
overflow-y: auto;
padding-right: 5px;
animation: fadeIn 0.7s ease;
}

.mini-calendar {
background: var(--bg-panel);
border: 1px solid var(--border);
border-radius: 16px;
padding: 16px;
backdrop-filter: var(--glass);
transition: all 0.3s ease;
}

.mini-calendar:hover {
border-color: rgba(255,255,255,0.15);
}

.calendar-header {
display: flex;
justify-content: space-between;
align-items: center;
margin-bottom: 12px;
}

.calendar-title {
font-size: 13px;
font-weight: 600;
color: var(--text-main);
}

.calendar-nav {
display: flex;
gap: 8px;
}

.calendar-nav button {
width: 24px;
height: 24px;
border: none;
background: rgba(255,255,255,0.05);
color: var(--text-muted);
border-radius: 6px;
cursor: pointer;
transition: all 0.2s;
display: grid;
place-items: center;
}

.calendar-nav button:hover {
background: rgba(255,255,255,0.1);
color: white;
}

.mini-calendar-grid {
display: grid;
grid-template-columns: repeat(7, 1fr);
gap: 4px;
text-align: center;
}

.mini-cal-header {
font-size: 10px;
color: var(--text-muted);
margin-bottom: 4px;
font-weight: 600;
}

.mini-cal-day {
aspect-ratio: 1;
display: grid;
place-items: center;
border-radius: 6px;
font-size: 11px;
cursor: pointer;
transition: all 0.2s;
position: relative;
}

.mini-cal-day:hover {
background: rgba(255,255,255,0.08);
}

.mini-cal-day.today {
background: var(--neon-blue);
color: white;
font-weight: bold;
box-shadow: 0 0 10px rgba(59, 130, 246, 0.4);
}

.mini-cal-day.has-task::after {
content: '';
position: absolute;
bottom: 2px;
width: 3px;
height: 3px;
background: var(--neon-pink);
border-radius: 50%;
}

.priority-chart {
background: var(--bg-panel);
border: 1px solid var(--border);
border-radius: 16px;
padding: 16px;
backdrop-filter: var(--glass);
}

.chart-title {
font-size: 11px;
color: var(--text-muted);
text-transform: uppercase;
letter-spacing: 1px;
margin-bottom: 12px;
font-weight: 600;
}

.chart-content {
display: flex;
align-items: center;
gap: 16px;
}

.mini-donut {
position: relative;
width: 80px;
height: 80px;
flex-shrink: 0;
}

.mini-donut svg {
width: 100%;
height: 100%;
}

.donut-center {
position: absolute;
top: 50%;
left: 50%;
transform: translate(-50%, -50%);
font-size: 18px;
font-weight: 700;
font-family: 'JetBrains Mono', monospace;
}

.mini-legend {
flex: 1;
display: flex;
flex-direction: column;
gap: 6px;
}

.legend-row {
display: flex;
justify-content: space-between;
align-items: center;
font-size: 11px;
}

.legend-label {
display: flex;
align-items: center;
gap: 6px;
}

.legend-dot {
width: 8px;
height: 8px;
border-radius: 50%;
}

.quick-actions {
background: var(--bg-panel);
border: 1px solid var(--border);
border-radius: 16px;
padding: 16px;
backdrop-filter: var(--glass);
}

.actions-title {
font-size: 11px;
color: var(--text-muted);
text-transform: uppercase;
letter-spacing: 1px;
margin-bottom: 12px;
font-weight: 600;
}

.actions-grid {
display: grid;
grid-template-columns: repeat(2, 1fr);
gap: 8px;
}

.action-btn {
background: var(--bg-panel-light);
border: 1px solid var(--border);
color: white;
padding: 10px;
border-radius: 10px;
cursor: pointer;
font-size: 11px;
display: flex;
flex-direction: column;
align-items: center;
gap: 6px;
transition: all 0.2s;
}

.action-btn:hover {
background: rgba(255,255,255,0.08);
border-color: rgba(255,255,255,0.2);
transform: translateY(-2px);
}

.action-btn svg {
width: 20px;
height: 20px;
}

.clock-widget {
background: var(--bg-panel);
border: 1px solid var(--border);
border-radius: 16px;
padding: 16px;
backdrop-filter: var(--glass);
text-align: center;
}

.clock-time {
font-family: 'JetBrains Mono', monospace;
font-size: 24px;
font-weight: 700;
margin-bottom: 4px;
background: linear-gradient(135deg, var(--neon-blue), var(--neon-purple));
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
background-clip: text;
}

.clock-date {
font-size: 11px;
color: var(--text-muted);
}

.task-header {
padding: 20px 24px;
border-bottom: 1px solid var(--border);
display: flex;
justify-content: space-between;
align-items: center;
}

.header-title h1 {
font-size: 20px;
font-weight: 700;
margin-bottom: 2px;
}

.header-title p {
font-size: 12px;
color: var(--text-muted);
}

.header-actions {
display: flex;
gap: 8px;
}

.header-btn {
padding: 8px 16px;
background: var(--bg-panel-light);
border: 1px solid var(--border);
border-radius: 8px;
color: white;
font-size: 12px;
cursor: pointer;
transition: all 0.2s;
display: flex;
align-items: center;
gap: 6px;
}

.header-btn:hover {
background: rgba(255,255,255,0.08);
border-color: rgba(255,255,255,0.2);
}

.header-btn svg {
width: 16px;
height: 16px;
}

.toolbar {
padding: 12px 24px;
display: flex;
gap: 12px;
border-bottom: 1px solid var(--border);
}

.search-input {
background: rgba(0,0,0,0.3);
border: 1px solid var(--border);
color: white;
padding: 8px 14px;
border-radius: 8px;
font-family: inherit;
width: 240px;
font-size: 13px;
transition: all 0.3s ease;
}

.search-input:focus {
border-color: var(--neon-blue);
width: 320px;
box-shadow: 0 0 0 2px rgba(59,130,246,0.2);
}

.task-scroll {
flex: 1;
overflow-y: auto;
padding: 16px 24px;
}

.task-card {
background: var(--bg-panel-light);
border-radius: 12px;
padding: 14px 18px;
margin-bottom: 8px;
display: flex;
align-items: center;
gap: 14px;
border: 1px solid transparent;
transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
opacity: 0;
animation: slideIn 0.3s ease forwards;
}

.task-card:hover {
background: rgba(255,255,255,0.05);
border-color: var(--border);
transform: translateX(8px);
box-shadow: 0 4px 12px rgba(0,0,0,0.2);
}

.checkbox {
width: 22px;
height: 22px;
border: 2px solid #555;
border-radius: 6px;
cursor: pointer;
display: grid;
place-items: center;
transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
flex-shrink: 0;
}

.checkbox:hover {
border-color: var(--neon-green);
}

.checkbox.checked {
background: var(--neon-green);
border-color: var(--neon-green);
transform: scale(1.1);
}

.checkbox svg {
transform: scale(0);
transition: transform 0.3s cubic-bezier(0.68, -0.55, 0.265, 1.55);
}

.checkbox.checked svg {
transform: scale(1);
}

.task-content {
flex: 1;
}

.task-main-text {
font-size: 14px;
font-weight: 500;
margin-bottom: 4px;
}

.task-sub-text {
font-size: 11px;
color: var(--text-muted);
display: flex;
align-items: center;
gap: 8px;
}

.tag {
padding: 2px 6px;
border-radius: 4px;
font-size: 9px;
font-weight: 700;
text-transform: uppercase;
letter-spacing: 0.5px;
}

.tag-high {
background: rgba(239, 68, 68, 0.15);
color: var(--neon-red);
}

.tag-med {
background: rgba(245, 158, 11, 0.15);
color: var(--neon-orange);
}

.tag-low {
background: rgba(59, 130, 246, 0.15);
color: var(--neon-blue);
}

.task-actions {
display: flex;
gap: 8px;
opacity: 0;
transition: opacity 0.2s;
}

.task-card:hover .task-actions {
opacity: 1;
}

.task-actions button {
background: none;
border: none;
color: #666;
cursor: pointer;
padding: 4px;
transition: all 0.2s;
border-radius: 4px;
}

.task-actions button:hover {
background: rgba(255,255,255,0.1);
color: white;
}

.task-actions button:last-child:hover {
color: var(--neon-red);
}

.fab {
position: fixed;
bottom: 30px;
right: 30px;
width: 56px;
height: 56px;
border-radius: 50%;
background: linear-gradient(135deg, var(--neon-blue), var(--neon-purple));
color: white;
border: none;
box-shadow: 0 10px 25px -5px rgba(139, 92, 246, 0.5);
cursor: pointer;
display: grid;
place-items: center;
transition: all 0.3s cubic-bezier(0.68, -0.55, 0.265, 1.55);
z-index: 50;
}

.fab:hover {
transform: scale(1.15) rotate(90deg);
box-shadow: 0 15px 35px -5px rgba(139, 92, 246, 0.7);
}

.fab:active {
transform: scale(1.05) rotate(90deg);
}

.modal-overlay {
position: fixed;
inset: 0;
background: rgba(0,0,0,0.8);
backdrop-filter: blur(5px);
z-index: 100;
display: none;
align-items: center;
justify-content: center;
animation: fadeIn 0.3s ease;
}

.modal-overlay.show {
display: flex;
}

.modal-box {
background: #18181b;
width: 450px;
padding: 30px;
border-radius: 20px;
border: 1px solid var(--border);
box-shadow: 0 0 50px rgba(0,0,0,0.5);
animation: scaleIn 0.3s cubic-bezier(0.68, -0.55, 0.265, 1.55);
}

.modal-title {
font-size: 22px;
font-weight: 700;
margin-bottom: 20px;
background: linear-gradient(135deg, var(--neon-blue), var(--neon-purple));
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
background-clip: text;
}

.input-group {
margin-bottom: 15px;
}

.input-label {
font-size: 11px;
color: #888;
display: block;
margin-bottom: 6px;
text-transform: uppercase;
letter-spacing: 1px;
font-weight: 600;
}

.full-input {
width: 100%;
background: #27272a;
border: 1px solid #3f3f46;
color: white;
padding: 10px 12px;
border-radius: 8px;
font-family: inherit;
font-size: 14px;
transition: all 0.2s;
}

.full-input:focus {
border-color: var(--neon-blue);
box-shadow: 0 0 0 2px rgba(59,130,246,0.2);
}

.modal-footer {
display: flex;
justify-content: flex-end;
gap: 10px;
margin-top: 20px;
}

.btn-secondary {
background: none;
border: none;
color: #888;
padding: 10px 20px;
cursor: pointer;
border-radius: 8px;
transition: all 0.2s;
}

.btn-secondary:hover {
background: rgba(255,255,255,0.05);
color: white;
}

.btn-primary {
background: linear-gradient(135deg, var(--neon-blue), var(--neon-purple));
color: white;
border: none;
padding: 10px 24px;
border-radius: 8px;
cursor: pointer;
font-weight: 600;
transition: all 0.2s;
}

.btn-primary:hover {
transform: translateY(-2px);
box-shadow: 0 5px 15px rgba(59,130,246,0.4);
}

@media (max-width: 1200px) {
.main-container {
grid-template-columns: 1fr 280px;
}
}

@media (max-width: 768px) {
.main-container {
grid-template-columns: 1fr;
}
.control-panel {
display: none;
}
}
</style>
</head>
<body>

<nav class="sidebar">
<div class="logo-box">
<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2.5">
<path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"></path>
</svg>
</div>
<div class="nav-icon active" title="All Tasks" onclick="filterTasks('all')">
<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
<rect x="3" y="3" width="7" height="7"></rect>
<rect x="14" y="3" width="7" height="7"></rect>
<rect x="14" y="14" width="7" height="7"></rect>
<rect x="3" y="14" width="7" height="7"></rect>
</svg>
</div>
<div class="nav-icon" title="Pending" onclick="filterTasks('pending')">
<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
<circle cx="12" cy="12" r="10"></circle>
<polyline points="12 6 12 12 16 14"></polyline>
</svg>
</div>
<div class="nav-icon" title="Completed" onclick="filterTasks('completed')">
<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
<path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
<polyline points="22 4 12 14.01 9 11.01"></polyline>
</svg>
</div>
<div style="margin-top:auto; padding-bottom: 20px;">
<a href="/logout" class="nav-icon" title="Logout">
<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#ef4444" stroke-width="2">
<path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path>
<polyline points="16 17 21 12 16 7"></polyline>
<line x1="21" y1="12" x2="9" y2="12"></line>
</svg>
</a>
</div>
</nav>

<div class="main-container">
<div class="top-stats-bar">
<div class="stat-card">
<div class="stat-label">Total Tasks</div>
<div class="stat-value" id="stat-total">0</div>
<div class="stat-trend">
<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3">
<polyline points="23 6 13.5 15.5 8.5 10.5 1 18"></polyline>
</svg>
<span id="stat-total-change">Loading...</span>
</div>
</div>

<div class="stat-card">
<div class="stat-label">Pending</div>
<div class="stat-value" style="color: var(--neon-orange);" id="stat-pending">0</div>
<div class="stat-trend" style="color: var(--neon-orange);">
<span id="stat-pending-change">Active</span>
</div>
</div>

<div class="stat-card">
<div class="stat-label">Completed</div>
<div class="stat-value" style="color: var(--neon-green);" id="stat-completed">0</div>
<div class="stat-trend">
<span id="stat-completed-change">0% completion</span>
</div>
</div>

<div class="stat-card">
<div class="stat-label">High Priority</div>
<div class="stat-value" style="color: var(--neon-red);" id="stat-high">0</div>
<div class="stat-trend" style="color: var(--neon-red);">
<span>Needs attention</span>
</div>
</div>
</div>

<section class="task-section">
<header class="task-header">
<div class="header-title">
<h1 id="page-title">All Tasks</h1>
<p>{{ session['users_name'] }}'s Workspace</p>
</div>
<div class="header-actions">
<button class="header-btn" onclick="exportToCSV()">
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
<polyline points="7 10 12 15 17 10"></polyline>
<line x1="12" y1="15" x2="12" y2="3"></line>
</svg>
Export
</button>
</div>
</header>

<div class="toolbar">
<input type="text" id="search-bar" class="search-input" placeholder="Search tasks..." onkeyup="renderList()">
</div>

<div id="task-list-container" class="task-scroll"></div>
</section>

<aside class="control-panel">
<div class="clock-widget">
<div class="clock-time" id="clock-time">00:00</div>
<div class="clock-date" id="clock-date">Loading...</div>
</div>

<div class="priority-chart">
<div class="chart-title">Priority Distribution</div>
<div class="chart-content">
<div class="mini-donut">
<svg viewBox="0 0 100 100">
<circle cx="50" cy="50" r="40" fill="none" stroke="rgba(255,255,255,0.05)" stroke-width="10"></circle>
<circle id="ring-high" cx="50" cy="50" r="40" fill="none" stroke="#ef4444" stroke-width="10" 
stroke-dasharray="251" stroke-dashoffset="251" transform="rotate(-90 50 50)"></circle>
<circle id="ring-med" cx="50" cy="50" r="40" fill="none" stroke="#f59e0b" stroke-width="10" 
stroke-dasharray="251" stroke-dashoffset="251" transform="rotate(-90 50 50)"></circle>
<circle id="ring-low" cx="50" cy="50" r="40" fill="none" stroke="#3b82f6" stroke-width="10" 
stroke-dasharray="251" stroke-dashoffset="251" transform="rotate(-90 50 50)"></circle>
</svg>
<div class="donut-center" id="total-count-center">0</div>
</div>
<div class="mini-legend">
<div class="legend-row">
<div class="legend-label">
<div class="legend-dot" style="background: #ef4444;"></div>
<span>High</span>
</div>
<span id="count-high">0</span>
</div>
<div class="legend-row">
<div class="legend-label">
<div class="legend-dot" style="background: #f59e0b;"></div>
<span>Medium</span>
</div>
<span id="count-med">0</span>
</div>
<div class="legend-row">
<div class="legend-label">
<div class="legend-dot" style="background: #3b82f6;"></div>
<span>Low</span>
</div>
<span id="count-low">0</span>
</div>
</div>
</div>
</div>

<div class="mini-calendar">
<div class="calendar-header">
<div class="calendar-title" id="cal-month-title">Calendar</div>
<div class="calendar-nav">
<button onclick="changeMonth(-1)">‹</button>
<button onclick="changeMonth(1)">›</button>
</div>
</div>
<div class="mini-calendar-grid">
<div class="mini-cal-header">S</div>
<div class="mini-cal-header">M</div>
<div class="mini-cal-header">T</div>
<div class="mini-cal-header">W</div>
<div class="mini-cal-header">T</div>
<div class="mini-cal-header">F</div>
<div class="mini-cal-header">S</div>
</div>
<div class="mini-calendar-grid" id="calendar-days"></div>
</div>

<div class="quick-actions">
<div class="actions-title">Quick Actions</div>
<div class="actions-grid">
<div class="action-btn" onclick="document.getElementById('name-modal').style.display='flex'">
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
<path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
<circle cx="12" cy="7" r="4"></circle>
</svg>
<span>Profile</span>
</div>
<div class="action-btn" onclick="clearCompleted()" style="color:#ef4444; border-color: rgba(239,68,68,0.3);">
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
<polyline points="3 6 5 6 21 6"></polyline>
<path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path>
</svg>
<span>Clear</span>
</div>
</div>
</div>
</aside>
</div>

<button class="fab" onclick="openModal()">
<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3">
<line x1="12" y1="5" x2="12" y2="19"></line>
<line x1="5" y1="12" x2="19" y2="12"></line>
</svg>
</button>

<div class="modal-overlay" id="task-modal">
<div class="modal-box">
<h2 class="modal-title">Task Details</h2>
<form id="task-form">
<input type="hidden" id="task-id">
<div class="input-group">
<label class="input-label">Title</label>
<input type="text" id="task-title" class="full-input" required>
</div>
<div class="input-group">
<label class="input-label">Description</label>
<input type="text" id="task-desc" class="full-input">
</div>
<div style="display:grid; grid-template-columns:1fr 1fr; gap:15px;">
<div class="input-group">
<label class="input-label">Due Date</label>
<input type="date" id="task-date" class="full-input">
</div>
<div class="input-group">
<label class="input-label">Priority</label>
<select id="task-priority" class="full-input">
<option value="high">High</option>
<option value="medium" selected>Medium</option>
<option value="low">Low</option>
</select>
</div>
</div>
<div class="modal-footer">
<button type="button" class="btn-secondary" onclick="closeModal()">Cancel</button>
<button type="submit" class="btn-primary">Save Task</button>
</div>
</form>
</div>
</div>

<div class="modal-overlay" id="name-modal">
<div class="modal-box" style="width:400px;">
<h3 class="modal-title">Update Profile</h3>
<form action="/change-name" method="post">
<div class="input-group">
<label class="input-label">Display Name</label>
<input type="text" name="new_name" class="full-input" placeholder="Enter your name" required>
</div>
<div class="modal-footer">
<button type="button" class="btn-secondary" onclick="document.getElementById('name-modal').style.display='none'">Cancel</button>
<button type="submit" class="btn-primary">Update</button>
</div>
</form>
</div>
</div>

<script>
let allTasks = [];
let currentFilter = 'all';
let currentMonth = new Date().getMonth();
let currentYear = new Date().getFullYear();

window.onload = () => {
initClock();
loadTasks();
renderCalendar();
};

async function loadTasks() {
try {
const res = await fetch('/api/tasks');
const data = await res.json();
if(data.success) {
allTasks = data.tasks;
renderList();
updateCharts();
updateStats();
renderCalendar();
}
} catch(e) { 
console.error('Error loading tasks:', e); 
}
}

function renderList() {
const container = document.getElementById('task-list-container');
const search = document.getElementById('search-bar').value.toLowerCase();

let tasks = allTasks.filter(t => {
const matchesFilter = currentFilter === 'all' ? true : t.status === currentFilter;
const matchesSearch = t.title.toLowerCase().includes(search);
return matchesFilter && matchesSearch;
});

tasks.sort((a,b) => (a.status === 'completed' ? 1 : -1));

if(tasks.length === 0) {
container.innerHTML = `<div style="text-align:center; padding:80px 20px; color:#555;">
<svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1" style="margin-bottom:16px; opacity:0.3;">
<circle cx="12" cy="12" r="10"></circle>
<line x1="12" y1="8" x2="12" y2="12"></line>
<line x1="12" y1="16" x2="12.01" y2="16"></line>
</svg>
<div style="font-size:16px; margin-bottom:8px;">No tasks found</div>
<div style="font-size:12px; color:#666;">Try adjusting your filters or create a new task</div>
</div>`;
return;
}

container.innerHTML = tasks.map((t, index) => {
const isDone = t.status === 'completed';
const pColor = t.priority === 'high' ? 'tag-high' : t.priority === 'low' ? 'tag-low' : 'tag-med';
const dateText = t.due_date ? `📅 ${t.due_date}` : '';

return `
<div class="task-card ${isDone ? 'completed' : ''}" style="opacity: ${isDone?0.6:1}; animation-delay: ${index * 0.05}s">
<div class="checkbox ${isDone?'checked':''}" onclick="toggleTask(${t.task_id})">
<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="4" stroke-linecap="round" stroke-linejoin="round">
<polyline points="20 6 9 17 4 12"></polyline>
</svg>
</div>
<div class="task-content">
<div class="task-main-text" style="text-decoration: ${isDone?'line-through':''}">${escapeHtml(t.title)}</div>
<div class="task-sub-text">
<span class="tag ${pColor}">${(t.priority||'med').toUpperCase()}</span>
${dateText ? `<span>${dateText}</span>` : ''}
</div>
</div>
<div class="task-actions">
<button onclick="editTask(${t.task_id})" title="Edit">
<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
<path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path>
<path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path>
</svg>
</button>
<button onclick="deleteTask(${t.task_id})" title="Delete">
<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
<polyline points="3 6 5 6 21 6"></polyline>
<path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path>
</svg>
</button>
</div>
</div>`;
}).join('');
}

function updateStats() {
const total = allTasks.length;
const pending = allTasks.filter(t => t.status === 'pending').length;
const completed = allTasks.filter(t => t.status === 'completed').length;
const high = allTasks.filter(t => t.priority === 'high' && t.status !== 'completed').length;

document.getElementById('stat-total').innerText = total;
document.getElementById('stat-pending').innerText = pending;
document.getElementById('stat-completed').innerText = completed;
document.getElementById('stat-high').innerText = high;

const completionRate = total > 0 ? Math.round((completed / total) * 100) : 0;
document.getElementById('stat-completed-change').innerText = `${completionRate}% completion`;
}

function updateCharts() {
const total = allTasks.length;
if(total === 0) {
document.getElementById('total-count-center').innerText = '0';
return;
}

const high = allTasks.filter(t => t.priority === 'high').length;
const med = allTasks.filter(t => t.priority === 'medium' || !t.priority).length;
const low = allTasks.filter(t => t.priority === 'low').length;

document.getElementById('total-count-center').innerText = total;
document.getElementById('count-high').innerText = high;
document.getElementById('count-med').innerText = med;
document.getElementById('count-low').innerText = low;

const C = 251;
const highLen = (high / total) * C;
const medLen = (med / total) * C;
const lowLen = (low / total) * C;

const rHigh = document.getElementById('ring-high');
rHigh.style.strokeDasharray = `${highLen} ${C}`;
rHigh.style.strokeDashoffset = 0;

const rMed = document.getElementById('ring-med');
rMed.style.strokeDasharray = `${medLen} ${C}`;
rMed.style.strokeDashoffset = -highLen;

const rLow = document.getElementById('ring-low');
rLow.style.strokeDasharray = `${lowLen} ${C}`;
rLow.style.strokeDashoffset = -(highLen + medLen);
}

function renderCalendar() {
const now = new Date(currentYear, currentMonth);
const year = now.getFullYear();
const month = now.getMonth();
const today = new Date().getDate();
const isCurrentMonth = (year === new Date().getFullYear() && month === new Date().getMonth());

document.getElementById('cal-month-title').innerText = now.toLocaleString('default', { month: 'short', year: 'numeric' });

const firstDay = new Date(year, month, 1).getDay();
const daysInMonth = new Date(year, month + 1, 0).getDate();
const container = document.getElementById('calendar-days');
container.innerHTML = '';

for(let i=0; i<firstDay; i++) {
container.innerHTML += `<div></div>`;
}

for(let i=1; i<=daysInMonth; i++) {
const currentStr = `${year}-${String(month+1).padStart(2,'0')}-${String(i).padStart(2,'0')}`;
const hasTask = allTasks.some(t => t.due_date === currentStr && t.status !== 'completed');
const isToday = (i === today && isCurrentMonth);

container.innerHTML += `
<div class="mini-cal-day ${isToday ? 'today' : ''} ${hasTask ? 'has-task' : ''}">
${i}
</div>
`;
}
}

function changeMonth(delta) {
currentMonth += delta;
if(currentMonth > 11) {
currentMonth = 0;
currentYear++;
} else if(currentMonth < 0) {
currentMonth = 11;
currentYear--;
}
renderCalendar();
}

function exportToCSV() {
let csvContent = "data:text/csv;charset=utf-8,ID,Title,Status,Priority,DueDate\\n";
allTasks.forEach(t => {
csvContent += `${t.task_id},"${t.title}",${t.status},${t.priority},${t.due_date}\\n`;
});
const encodedUri = encodeURI(csvContent);
const link = document.createElement("a");
link.setAttribute("href", encodedUri);
link.setAttribute("download", "tasks_export.csv");
document.body.appendChild(link);
link.click();
document.body.removeChild(link);
}

async function clearCompleted() {
const completed = allTasks.filter(t => t.status === 'completed');
if(completed.length === 0) {
alert("No completed tasks to clear.");
return;
}
if(!confirm(`Delete ${completed.length} completed task(s)?`)) return;

for(const t of completed) {
await fetch(`/api/tasks/${t.task_id}`, { method: 'DELETE' });
}
loadTasks();
}

async function toggleTask(id) {
await fetch(`/api/tasks/${id}/toggle`, { method: 'POST' });
loadTasks();
}

async function deleteTask(id) {
if(confirm('Delete this task?')) {
await fetch(`/api/tasks/${id}`, { method: 'DELETE' });
loadTasks();
}
}

let isEditing = false;

function openModal() {
isEditing = false;
document.getElementById('task-form').reset();
document.getElementById('task-modal').classList.add('show');
document.getElementById('task-modal').style.display = 'flex';
}

function closeModal() {
document.getElementById('task-modal').classList.remove('show');
setTimeout(() => {
document.getElementById('task-modal').style.display = 'none';
}, 300);
}

function editTask(id) {
const t = allTasks.find(x => x.task_id === id);
if(!t) return;
isEditing = true;
document.getElementById('task-id').value = t.task_id;
document.getElementById('task-title').value = t.title;
document.getElementById('task-desc').value = t.description || '';
document.getElementById('task-date').value = t.due_date || '';
document.getElementById('task-priority').value = t.priority || 'medium';
document.getElementById('task-modal').classList.add('show');
document.getElementById('task-modal').style.display = 'flex';
}

document.getElementById('task-form').onsubmit = async (e) => {
e.preventDefault();
const data = {
title: document.getElementById('task-title').value,
description: document.getElementById('task-desc').value,
due_date: document.getElementById('task-date').value,
priority: document.getElementById('task-priority').value
};
const url = isEditing ? `/api/tasks/${document.getElementById('task-id').value}` : '/api/tasks';
const method = isEditing ? 'PUT' : 'POST';

await fetch(url, { 
method, 
headers: {'Content-Type':'application/json'}, 
body: JSON.stringify(data) 
});
closeModal();
loadTasks();
};

function filterTasks(f) {
currentFilter = f;
document.querySelectorAll('.nav-icon').forEach((el, idx) => {
if(idx < 3) el.classList.remove('active');
});
event.currentTarget.classList.add('active');

const titles = {
'all': 'All Tasks',
'pending': 'Pending Tasks',
'completed': 'Completed Tasks'
};
document.getElementById('page-title').innerText = titles[f] || 'Tasks';

renderList();
}

function initClock() {
const updateClock = () => {
const now = new Date();
document.getElementById('clock-time').innerText = now.toLocaleTimeString('en-GB', {
hour:'2-digit', 
minute:'2-digit'
});
document.getElementById('clock-date').innerText = now.toLocaleDateString('en-US', {
weekday:'short', 
month:'short', 
day:'numeric'
});
};
updateClock();
setInterval(updateClock, 1000);
}

function escapeHtml(text) {
const div = document.createElement('div');
div.textContent = text;
return div.innerHTML;
}

document.getElementById('task-modal').addEventListener('click', (e) => {
if(e.target.id === 'task-modal') closeModal();
});

document.getElementById('name-modal').addEventListener('click', (e) => {
if(e.target.id === 'name-modal') {
document.getElementById('name-modal').style.display = 'none';
}
});
</script>
</body>
</html>
"""
