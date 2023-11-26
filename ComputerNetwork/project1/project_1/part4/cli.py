import smtplib
smtpServer = "smtp.gmail.com"
smtpPort = 587
userName = input("enter your username: ")
password = input("enter your password: ")
recieverUser = input("enter reciever's useranme: ")
subject = "Subject: " + input("enter subject: ") + "\r\n\r\n"
msg = input("enter your mssage: ")
server = smtplib.SMTP(smtpServer, smtpPort)
server.ehlo()
server.starttls()
server.ehlo()
server.login(userName, password)
server.sendmail(userName, recieverUser, subject + msg)
server.close()
