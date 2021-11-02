#! /usr/bin/python

# -*- coding:utf-8 -*-

"""
    @author: 罗从良
    @email: rontomai@gmail.com
    @create_time: 2018-10-31
"""

__version__ = "0.1"
__author__ = "罗从良"
__email__ = "admin@akaros.cn"


import os

from flask import Flask, render_template, request
from flask_script import Manager
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from threading import Thread
import config


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.secret_key = config.SECRET_KEY
app.config['DEBUG'] = True


app.config['MAIL_DEBUG'] = True             # 开启debug，便于调试看信息
app.config['MAIL_SUPPRESS_SEND'] = False    # 发送邮件，为True则不发送
app.config['MAIL_SERVER'] = 'smtp.exmail.qq.com'   # 邮箱服务器
app.config['MAIL_PORT'] = 465               # 端口
app.config['MAIL_USE_SSL'] = True           # 重要，qq邮箱需要使用SSL
app.config['MAIL_USE_TLS'] = False          # 不需要使用TLS
app.config['MAIL_USERNAME'] = 'consult@carf-enna.com'  # 填邮箱
app.config["MAIL_PASSWORD"] = "ramMFhegq4Q2RXC5"      # 填授权码
app.config['MAIL_DEFAULT_SENDER'] = 'consult@carf-enna.com'  # 填邮箱，默认发送者

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

manager = Manager(app)
mail = Mail(app)
db = SQLAlchemy(app)
migrate = Migrate(app)


# 异步发送邮件
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


@app.route('/send')
def send():
    msg = Message(subject='Hello World',
                  sender="consult@carf-enna.com",  # 需要使用默认发送者则不用填
                  recipients=['724261350@qq.com', 'market@carf-enna.com'])
    # 邮件内容会以文本和html两种格式呈现，而你能看到哪种格式取决于你的邮件客户端。
    msg.body = '邮件测试测试'
    msg.html = '<b>测试测试发送邮件<b>'
    thread = Thread(target=send_async_email, args=[app, msg])
    thread.start()
    return '<h1>邮件发送成功</h1>'


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    # email = request.form['email'].strip()
    # subject = 'Hello'
    # message = '這是 flask-mail example <br> <br>' \
    #           '附上一張圖片 <br> <br>' \
    #           '<b  style="color:#FF4E4E" >新垣結衣</b>'
    # msg = Message(
    #     subject=subject,
    #     recipients=[email],
    #     html=message
    # )
    # # msg.body = '純文字'
    # with app.open_resource("static/images/image.jpg") as fp:
    #     msg.attach("image.jpg", "image/jpg", fp.read())
    # mail.send(msg)

    # return "請到你的信箱收信~ ^0^"
    return render_template("contact.html")
    # form = ContactForm()
    # print(form)

    # form = LoginForm()
    # if form.validate_on_submit():
    #     user = User.query.filter_by(username=form.username.data).first()
    #     if user is None or not user.check_password(form.password.data):
    #         flash('Invalid username or password')
    #         return redirect(url_for('auth.login'))
    #     login_user(user, remember=form.remember_me.data)
    #     next_page = request.args.get('next')
    #     if not next_page or url_parse(next_page).netloc != '':
    #         next_page = url_for('admin.admin')
    #     return redirect(next_page)
    #
    # if form.validate_on_submit():
    #     print("ALL OK, SEND EMAIL")
        # message = "Email: %s -- Message: %s" % (form.email.data, form.message.data)
        # msg = Message(subject='Hello World',
        #               sender=form.email.data,  # 需要使用默认发送者则不用填
        #               recipients=['admin@akaros.cn'])
        # # 邮件内容会以文本和html两种格式呈现，而你能看到哪种格式取决于你的邮件客户端。
        # msg.body = form.message.data
        # msg.html = '<h1>'+form.message.data+'</h1>'
        # thread = Thread(target=send_async_email, args=[app, msg])
        # thread.start()
        # # return '<h1>邮件发送成功</h1>'
        # # msg = MIMEText(message, 'text')
        # # msg['Subject'] = config.EMAIL_SUBJECT
        # # msg['From'] = config.SMTP_USER
        # # msg['To'] = config.SMTP_USER
        # # smtp = None
        # # if config.SMTP_TLS:
        # #     smtp = smtplib.SMTP_SSL(config.SMTP_HOST, config.SMTP_PORT)
        # # else:
        # #     smtp = smtplib.SMTP(config.SMTP_HOST, config.SMTP_PORT)
        # # smtp.login(config.SMTP_USER, config.SMTP_PASS)
        # # smtp.login(config.SMTP_USER, config.SMTP_PASS)
        # # smtp.sendmail(config.SMTP_USER, [config.SMTP_USER], msg.as_string())
        # # flash("完成了发送！")
        # # smtp.quit()
        # return redirect(url_for('index'))
    # return render_template("contact.html")


# 下面相当邮箱订阅情况
@app.route("/send_mail", methods=['POST'])
def send_mail():
    email = request.form['email'].strip()
    subject = 'Hello'
    message = '這是 flask-mail example <br> <br>' \
              '附上一張圖片 <br> <br>' \
              '<b  style="color:#FF4E4E" >新垣結衣</b>'
    msg = Message(
        subject=subject,
        recipients=[email],
        html=message
    )
    # msg.body = '純文字'
    with app.open_resource("static/images/image.jpg") as fp:
        msg.attach("image.jpg", "image/jpg", fp.read())
    thread = Thread(target=send_async_email, args=[app, msg])
    thread.start()
    # mail.send(msg)

    # return "請到你的信箱收信~ ^0^"
    return render_template("ok.html")


# 多邮件分发
@app.route("/bulk_emails")
def bulk_emails():
    """批次寄信"""
    users = [
        {"name": "xxxxxxxxxx", "email": "xxxxxxxxxx"},
        {"name": "xxxxxxxxxx", "email": "xxxxxxxxxx"},
        {"name": "xxxxxxxxxx", "email": "xxxxxxxxxx"},
        {"name": "xxxxxxxxxx", "email": "xxxxxxxxxx"},
        {"name": "xxxxxxxxxx", "email": "xxxxxxxxxx"},
        {"name": "xxxxxxxxxx", "email": "xxxxxxxxxx"},
    ]

    with mail.connect() as conn:
        for user in users:
            subject = 'hello, {}'.format(user['name'])

            message = '這是 flask-mail example <br> <br>' \
                      '附上一張圖片 <br> <br>' \
                      '<b  style="color:#FF4E4E" >新垣結衣</b>'
            msg = Message(subject=subject,
                          recipients=[user['email']],
                          html=message,
                          )
            # msg.body = '純文字'
            with app.open_resource("static/image.jpg") as fp:
                msg.attach("image.jpg", "image/jpg", fp.read())
            conn.send(msg)

    return "請到你的信箱收信~ ^0^"


@app.route("/service")
def service():
    return render_template("service.html")


if __name__ == '__main__':
    manager.run()

