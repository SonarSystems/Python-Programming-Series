#!/usr/bin/python

import Cookie

cook = Cookie.SimpleCookie()
cook["UserID"] = "Frahaan"
cook["UserID"]["expires"] = 60 * 60 * 24

print (cook)
 
print ("Content-type:text/html\r\n\r\n")

print ("<html>")
print ("<head>")
print ("<title>My First CGI App</title>")
print ("</head>")
print ("<body>")
print ("<h3>This is HTML's Body Section</h3>")
print (cook["UserID"].value)
print ("</body>")
print ("</html>")