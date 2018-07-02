#!/usr/bin/python3

import pymysql

db = pymysql.connect("localhost", "root", "", "users")

cursor = db.cursor()

sql = "DELETE FROM TestTable WHERE Name = 'hello'"

try:
   cursor.execute(sql)

   db.commit()
except:
   db.rollback()
        
db.close()
