import email
import random
import smtplib
from email.message import EmailMessage

# 从我们封装好的数据库工具里引入函数
from 敏捷.敏捷管理2.db_ops import otp_save, otp_verify, user_exists, user_save

# ====== 发件邮箱配置（与你之前保持一致）======
SENDER_EMAIL = "2775968902a@gmail.com"
APP_PASSWORD = "rqprxiiragfnmcvr"   # Gmail App Password

def send_email_code_real(to_email: str, ttl: int = 300) -> bool:
    """
    生成验证码 -> 先写入 MySQL 的 email_otp -> 再发邮件
    """
    #验证码
    code = f"{random.randint(0, 999999):06d}"

    # 1) 验证码写入数据库（email_otp）
    otp_save(to_email, code, ttl)

    # 2) 发邮件
    msg = EmailMessage()
    msg["From"] = SENDER_EMAIL
    msg["To"] = to_email
    msg["Subject"] = "注册验证码"
    msg.set_content(f"您的验证码: {code}\n{ttl//60} 分钟内有效")

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=15) as smtp:
            smtp.login(SENDER_EMAIL, APP_PASSWORD)
            smtp.send_message(msg)
        return True
    except Exception as e:
        return False

def start_registration(email:str,ttl:int=300) -> tuple[bool,str]:
    if user_exists(email):
        return False,"该邮箱已被注册"

    ok=send_email_code_real(email, ttl=ttl)
    if not ok:
        return False,"发送失败"
    else:
        return True,"发送成功"

def finsh_registration(email:str,code:str,password,username,ttl:int=300) -> tuple[bool,str]:

    ok_code=otp_verify(email,code)
    ok_save=user_save(email, username, password)

    if not ok_code:
        return False,"验证码错误"
    else:
        if not ok_save:
            return False,"数据保存失败"
        else :
            return True,"注册成功"


