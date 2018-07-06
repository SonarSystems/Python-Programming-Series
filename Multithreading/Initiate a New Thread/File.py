#!/usr/bin/python3

import _thread
import time

def TimeFunc( thread, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % (thread, time.ctime(time.time())))

try:
   _thread.start_new_thread( TimeFunc, ("Thread Number 1", 2, ) )
   _thread.start_new_thread( TimeFunc, ("Thread Number 2", 2, ) )
except:
   print ("Error: unable to start thread")

while 1:
   pass
