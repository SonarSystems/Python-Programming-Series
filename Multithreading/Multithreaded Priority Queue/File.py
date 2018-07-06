#!/usr/bin/python3

import queue
import threading
import time

exitFlag = 0

class EpicThread(threading.Thread):
   def __init__(self, threadID, name, q):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.q = q
   def run(self):
      print ("Starting " + self.name)
      ProcessData(self.name, self.q)
      print ("Exiting " + self.name)

def ProcessData(threadName, q):
   while not exitFlag:
      queueLock.acquire()
      if not workQueue.empty():
         data = q.get()
         queueLock.release()
         print ("%s processing %s" % (threadName, data))
      else:
         queueLock.release()
         time.sleep(1)

threadList = ["Thread 1", "Thread 2", "Thread 3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

for tName in threadList:
   thread = EpicThread(threadID, tName, workQueue)
   thread.start()
   threads.append(thread)
   threadID += 1

queueLock.acquire()
for word in nameList:
   workQueue.put(word)
queueLock.release()

while not workQueue.empty():
   pass

exitFlag = 1

for t in threads:
   t.join()
print ("Exiting Main Thread")
