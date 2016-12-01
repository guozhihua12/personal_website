#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from email.mime.multipart import MIMEMultipart
# from email.mime.base import MIMEBase
# from email.MIMEText import MIMEText
from email.mime.text import MIMEText
 
# python 2.3.*: email.Utils email.Encoders
from email.utils import COMMASPACE,formatdate
from email import encoders
from email.header import Header


import os
 
#server['name'], server['user'], server['passwd']

from django.conf import settings

server = {
    'name': getattr(settings, 'email_server', 'smtp.qq.com'),
    'user': getattr(settings, 'email_user', '312736700@qq.com'),
    'passwd': getattr(settings, 'email_passwd', 'xxx'),
}


def send_mail(fro, subject, text, files=[],
              server=server):
    # assert type(server) == dict
    # assert type(to) == list
    # assert type(files) == list
 
    msg = MIMEMultipart() 
    # msg['From'] = fro
    msg['Content-Type'] = 'Text/HTML'
    msg['From'] = server.get('user')
    # msg['Subject'] = subject
    msg['Subject'] = Header(subject, 'gb2312')
    msg['To'] = msg['From']
    # msg['To'] = COMMASPACE.join(to) #COMMASPACE==', '
    msg['Date'] = formatdate(localtime=True) 
    msg.attach(MIMEText(text.encode('gb2312')))
 
    # for file in files:
    #     part = MIMEBase('application', 'octet-stream') #'octet-stream': binary data
    #     part.set_payload(open(file, 'rb'.read()))
    #     encoders.encode_base64(part)
    #     part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(file))
    #     msg.attach(part)
 
    import smtplib 
    # smtp = smtplib.SMTP(server['name'])
    smtp = smtplib.SMTP_SSL(server['name'], 465)
    smtp.login(server['user'], server['passwd']) 
    smtp.sendmail(fro, server['user'], msg.as_string())
    smtp.close()