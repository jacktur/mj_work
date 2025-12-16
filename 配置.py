# config.py - 应用配置文件
from datetime import timedelta


class Config:
    """Flask应用配置类"""

    # Flask基础配置
    SECRET_KEY = "dev-123"  # 生产环境请使用随机生成的密钥
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=30)

    # 调试模式
    DEBUG = True

    # 服务器配置
    HOST = "127.0.0.1"
    PORT = 5000

    # 验证码配置
    OTP_TTL = 300  # 验证码有效期(秒)

    # 邮件配置
    SENDER_EMAIL = "2775968902a@gmail.com"
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 465


class ProductionConfig(Config):
    """生产环境配置"""
    DEBUG = False
    # 这里应该从环境变量读取
    SECRET_KEY = "your-production-secret-key-here"


class DevelopmentConfig(Config):
    """开发环境配置"""
    DEBUG = True


# 默认使用开发环境配置
config = DevelopmentConfig()