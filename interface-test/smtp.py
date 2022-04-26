# -*- coding: UTF-8 -*-
import smtplib
import ssl
from email.mime.text import MIMEText

def test():
    sender = '2651932824@qq.com'
    password = ''
    receiver = '2651932824@qq.com'
    content = 'python发送qq'

    smtp_server = "smtp.qq.com"
    port = 465

    subject = "我在学习Python发送QQ邮件"
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    try:
        server = smtplib.SMTP_SSL(smtp_server, port)
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())
        server.quit()
    except Exception as e:
        print("发送失败了")
        print(e)
        return {'err': 1}

    return {'err': 0}

if __name__ == '__main__':
    test()