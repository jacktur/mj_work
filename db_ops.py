# db_ops.py —— MySQL 读写 & 密码哈希（与你当前表结构匹配）
import os, hmac, hashlib
from datetime import datetime, timedelta
import pymysql
from pymysql.cursors import DictCursor

DB_CONFIG = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "2775968902",
    "database": "敏捷管理",
    "charset": "utf8mb4",
    "cursorclass": DictCursor,
    "autocommit": True,
}

def get_conn():
    return pymysql.connect(**DB_CONFIG)

# === 密码哈希 / 校验 ===
def hash_password(password: str, salt: bytes | None = None, iterations: int = 120_000):
    if salt is None:
        salt = os.urandom(16)  # 随机取16字节作为盐
    pwd_hash = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, iterations)
    return pwd_hash, salt, iterations

def verify_password(password: str, stored_hash: bytes, salt: bytes, iterations: int) -> bool:
    test_hash = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, iterations)
    return hmac.compare_digest(test_hash, stored_hash)

# === register 表 ===
TABLE_USERS = "register"

# 验证邮箱是否存在
def user_exists(email: str) -> bool:
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute(f"SELECT 1 FROM `{TABLE_USERS}` WHERE `Email`=%s", (email,))
        return cur.fetchone() is not None

# 用户保存
def user_save(email: str, username: str, password: str) -> bool:
    if user_exists(email):
        return False  # 删除 print
    pwd_hash, salt, iterations = hash_password(password)
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute(
            f"INSERT INTO `{TABLE_USERS}` "
            f"(`Email`,`Users_name`,`password_hash`,`salt`,`iterations`,`created_at`) "
            f"VALUES (%s,%s,%s,%s,%s,NOW())",
            (email, username, pwd_hash, salt, iterations),
        )
    return True  # 删除 print

# 用户名更改
def user_name_change(email: str, new_username: str) -> bool:
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute(
            f"UPDATE `{TABLE_USERS}` "
            f"SET `Users_name`=%s "
            f"WHERE `Email`=%s ",
            (new_username, email),
        )
        affected_rows = cur.rowcount
        conn.commit()
    return affected_rows > 0

def user_get(email: str):
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute(
            f"SELECT `id`,`Email`,`Users_name`,`password_hash`,`salt`,`iterations` "
            f"FROM `{TABLE_USERS}` WHERE `Email`=%s",
            (email,),
        )
        return cur.fetchone()

# 验证码的保存
def otp_save(email: str, code: str, ttl_sec: int = 300):
    from datetime import datetime, timedelta
    expire_at = datetime.now() + timedelta(seconds=ttl_sec)
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute(
            "INSERT INTO `email_otp`(`email`,`code`,`expire_at`) "
            "VALUES (%s,%s,%s) "
            "ON DUPLICATE KEY UPDATE `code`=VALUES(`code`), `expire_at`=VALUES(`expire_at`)",
            (email, code, expire_at),
        )

# 验证码的识别
def otp_verify(email: str, code: str, max_tries: int = 5) -> bool:
    from datetime import datetime
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute("SELECT `code`,`expire_at` FROM `email_otp` WHERE `email`=%s", (email,))
        row = cur.fetchone()
        if not row:
            return False
        if row["expire_at"] < datetime.now():
            cur.execute("DELETE FROM `email_otp` WHERE `email`=%s", (email,))
            return False
        if code.strip() == row["code"]:
            cur.execute("DELETE FROM `email_otp` WHERE `email`=%s", (email,))
            return True
        else:
            return False

# ================== 任务：创建 / 查询 ==================
