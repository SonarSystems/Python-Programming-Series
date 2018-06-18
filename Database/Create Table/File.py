#!/usr/bin/python3

import pymysql

# Put your servers name, username, password and database details here
db = pymysql.connect("localhost","root","","users" )

cursor = db.cursor()

sql = """CREATE TABLE TestTable (
   name  CHAR(20) NOT NULL,
   location CHAR(100),  
   gender CHAR(1),
   age INTEGER )"""

cursor.execute(sql)

db.close()
