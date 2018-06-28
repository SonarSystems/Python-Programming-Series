#!/usr/bin/python3

import pymysql

db = pymysql.connect("localhost", "root", "", "users")

cursor = db.cursor()

sql = """INSERT INTO TestTable(
    name, location, gender, age)
    VALUES ('Frahaan', 'UK', 'M', 26)"""

try:
   cursor.execute(sql)

   db.commit()
except:
   db.rollback()

cursor.execute(sql)

db.close()
