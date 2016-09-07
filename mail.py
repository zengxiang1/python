#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

class Mail(object):
	"""
	param:server,port username,password
	"""
	def __init__(self,server,port,username,password):
		self.server = server
		self.username = username
		self.password = password
		try:
			self.smtp =smtplib.SMTP()
			self.smtp.connect(server,port)
			self.smtp.starttls()
			self.smtp.login(username,password)
			print '-----------------Login Success--------------'
			print 'call send(toaddr,subject,msg) to send email'
		except:
			print '-----------------Login Fail------------------'
			print '-please check your account or confirm smtp server is on'
	def send(self,toAddr,subject,msg):
		message = MIMEText(msg, 'plain', 'utf-8')
		message['To'] =  Header(toAddr,'utf-8')
		message['From'] = Header(self.username,'utf-8')
		message['Subject'] = Header(subject,'utf-8')
		self.smtp.sendmail(self.username,toAddr,message.as_string())


if __name__ == '__main__':
	mail = Mail('smtp.qq.com',587,'190093037@qq.com','hgivgnncysjvbhei')
	mail.send('3217330733@qq.com','hahaha','meto')	
# To = "3217330733@qq.com"
# server = 'smtp.qq.com'
# From = "190093037@qq.com"
# token = "axyladhqpniwbgda"

# message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
# message['To'] =  To

# subject = 'Python SMTP 邮件测试'
# message['Subject'] = "test"

# smtp =smtplib.SMTP()
# smtp.connect(server,587)
# smtp.starttls()
# smtp.login(From,'lipcwayzdophcaej')
# smtp.sendmail(From,To,message.as_string())

