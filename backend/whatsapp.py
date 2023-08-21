#!/usr/bin/python3

import cgi
#import pywhatkit

print("Content-type: text/html")
print()


mydata = cgi.FieldStorage()
phn = mydata.getvalue("phn")
msg = mydata.getvalue("msg")

#pywhatkit.sendwhatmsg_instantly(phn,msg)
print("<body align='center'>")
print("<h1> {} </h1>".format(msg))
print()
print("MESSAGE SENT SUCCESSFULLY")
print("</body>")
