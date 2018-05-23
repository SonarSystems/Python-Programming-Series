import re

string1 = "Hello world is awesome"

result = re.search(r'(.*) world (.*?) .*', string1, re.M|re.I)

if (result):
  print(result.group())
  print(result.group(1))
  print(result.group(2))
else:
  print("No result")