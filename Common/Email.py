# -*- coding: utf-8 -*-

"""
封装发送邮件的方法

"""
import smtplib
import time, os, codecs
from email.header import Header
from email.mime.text import MIMEText

from Common import Log
from Common.Config import Config


class SendMail:

    def __init__(self):
        self.config = Config()
        self.log = Log.MyLog()

    def sendMail(self):
        smtpserver = self.config.get_conf('mail', 'smtpserver')
        sender = self.config.get_conf('mail', 'sender')
        receiver = self.config.get_conf('mail', 'receiver')
        username = self.config.get_conf('mail', 'username')
        password = self.config.get_conf('mail', 'password')

        report_path = os.path.dirname(os.path.dirname(__file__)) + '\\Report\\report.html'
        with codecs.open(report_path, 'r', 'utf-8') as f:
            mail_body = f.read()
        msg = MIMEText(mail_body, "html", "utf-8")

        tm = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        subject = "自动化测试报告_" + tm
        msg['Subject'] = Header(subject, 'utf-8')
        msg['From'] = sender
        receivers = receiver
        toclause = receivers.split(',')
        msg['To'] = ",".join(toclause)

        try:
            smtp = smtplib.SMTP()
            smtp.connect(smtpserver)
            smtp.login(username, password)
            smtp.sendmail(sender, toclause, msg.as_string())
            print("发送成功")
            self.log.info("邮件发送成功")
        except Exception as e:
            print(e)
            print("发送失败")
            self.log.error("邮件发送失败，请检查邮件配置")


if __name__ == '__main__':
    s = SendMail()
    s.sendMail()
