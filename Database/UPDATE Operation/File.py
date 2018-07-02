#!/usr/bin/python3

import pymysql

db = pymysql.connect("localhost", "root", "", "users")

cursor = db.cursor()

sql = "UPDATE TestTable SET Age = 30 WHERE Name = 'Frahaan'"

try:
   cursor.execute(sql)

   db.commit()
except:
   db.rollback()
        

db.close()
