# coding: utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import sys
def email(msgs = '不是传参'):
    print msgs
    sender = 'zhoujianwen@haoqiao.com'
    receiver = '277409155@qq.com'
    subject = '测试邮件主题'
    smtpserver = 'smtp.exmail.qq.com'
    username = '820631572@qq.com'
    password = 'Zjw478123552'
    msg = MIMEText(msgs, 'text', 'utf-8')  # 中文需参数‘utf-8’，单字节字符不需要
    msg['Subject'] = Header(subject, 'utf-8')

    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    smtp.close()
    print '发送成功'
email('Traceback (most recent call last):\n \
  File "/opt/space/urllib1/hq/my_excepthook/test_excepthool_package/hq_excepthook.py", line 102, in Process_run\n \
    self._target(*self._args, **self._kwargs)\
  File "/opt/space/urllib1/hq/my_excepthook/run_type/more_process/more_process.py", line 13, in worker\n \
    1 / 0\n \
ZeroDivisionError: integer division or modulo by zero\n \
')
# email(sys.argv[1])