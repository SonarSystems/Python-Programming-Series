#!/usr/bin/python3

import pymysql

db = pymysql.connect("localhost", "root", "", "users")

cursor = db.cursor()

sql = "SELECT * FROM TestTable"

try:
   cursor.execute(sql)

   results = cursor.fetchall()
   
   for row in results:
      name = row[0]
      location = row[1]
      gender = row[2]
      age = row[3]

      print ("Name: %s, Location: %s, Gender: %s, Age: %s" % (name, location, gender, age))
except:
   print ("Error: unable to fetch data")
        

db.close()
