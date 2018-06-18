#!/usr/bin/python3

import pymysql

# Put your servers name, username, password and database details here
db = pymysql.connect("localhost","root","","users" )

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()
print ("Database Version : %s " % data)

db.close()
