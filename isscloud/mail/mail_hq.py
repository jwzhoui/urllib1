#!/usr/bin/python
# -*- coding=utf-8 -*-

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import traceback

__MAIL_CONF = dict()
__MAIL_CONF["smtp_server"] = "smtp.exmail.qq.com"
__MAIL_CONF["user"] = "zhoujianwen@haoqiao.com"
__MAIL_CONF["pwd"] = "Zjw478123552"
__MAIL_CONF["From"] = "zhoujianwen@haoqiao.com"

MAIL_LIST = ['277409155@qq.com']


def send_mail_to(subject, message, to_list=MAIL_LIST):
    try:
        smtp_client = smtplib.SMTP(__MAIL_CONF["smtp_server"])
        smtp_client.login(__MAIL_CONF["user"], __MAIL_CONF["pwd"])

        send_msg = MIMEMultipart()
        html_att = MIMEText(message, 'plain', 'utf-8')
        send_msg.attach(html_att)

        send_msg["Accept-Language"] = "zh-CN"
        send_msg["Accept-Charset"] = "ISO-8859-1,utf-8"
        send_msg['Subject'] = Header(subject, 'utf-8')
        send_msg['From'] = __MAIL_CONF["From"]
        send_msg['To'] = ';'.join(to_list)
        send_msg['Cc'] = ''

        smtp_client.sendmail(__MAIL_CONF["From"], to_list, send_msg.as_string())
        smtp_client.close()
        return True
    except:
        print traceback.format_exc()
        return False


def __main__():
    reload(sys)
    sys.setdefaultencoding('utf-8')

    # to_list = ['277409155@qq.com','820631572@qq.com']
    if not send_mail_to('测试', '邮件内容'):
        print "send_mail_to failed"

if __name__ == "__main__":
    __main__()
