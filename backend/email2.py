#!/usr/bin/python3

import smtplib
import cgi

print("Content-type: text/html")
print()

print("<h3 align='center'>")
print("mail sent successfully")
print("</h3>")
data=cgi.FieldStorage()
sender_email=data.getvalue('semail')
password=data.getvalue('pass')
reciever=data.getvalue('remail')
message=data.getvalue('msg')
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender_email,password)
server.sendmail(sender_email,reciever, message)
print(email)
