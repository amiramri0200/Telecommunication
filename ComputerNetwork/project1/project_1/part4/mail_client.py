#!/usr/bin/python3 
import smtplib, imaplib, email

username = input('user name: ')
password = input('password: ')

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(username, password)

subject = input('subject: ')
message = input('message:\n')
recipient = input('recipient: ')
header = 'to:' + recipient + '\n' + 'from:' + username + '\n' + 'subject:' + subject
content = header + '\n' + message + '\n'
server.sendmail(username, recipient, content)
print("your email has been sent successfuly")

