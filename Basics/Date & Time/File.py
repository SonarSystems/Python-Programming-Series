import time 
import calendar

# Ticks
var1 = time.time()
print(var1)

# Local Time
local = time.localtime(time.time())
print(local)

# Formatted Time
timeLocal = time.asctime(time.localtime(time.time()))
print(timeLocal)

# Calendars
calendarVar = calendar.month(2008, 1)
print(calendarVar)