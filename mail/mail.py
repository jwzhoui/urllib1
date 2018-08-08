# coding: utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import sys
def email(msgs = '不是传参'):
    print msgs
    sender = 'jwzhoui@isoftstone.com'
    receiver = 'zhoujianwen_emainl@yeah.net'
    subject = '测试邮件主题'
    smtpserver = 'smtp.isoftstone.com'
    username = 'jwzhoui@isoftstone.com'
    password = 'xhk#wf8d'
    msg = MIMEText(msgs, 'text', 'utf-8')  # 中文需参数‘utf-8’，单字节字符不需要
    msg['Subject'] = Header(subject, 'utf-8')

    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    ss = smtp.close()
    print '发送成功'
email(sys.argv[1])