import os
basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'asdfasfqwerqwerasdfasdfas阿斯顿发送到发送的阿斯顿发送到发'
SMTP_HOST = 'smtp.qq.com'
SMTP_USER = '724261350'
SMTP_PASS = 'bdhxcrdqhdctbeeh'
SMTP_PORT = 465
SMTP_TLS = True
EMAIL_SUBJECT = '测试连接页面'
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False


# 插入本地设置的方式
# try:
#     from local_settings import *
# except:
#     pass
