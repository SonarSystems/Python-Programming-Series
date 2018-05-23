import re

string1 = "23fs428\634iuo923 . 32'';423[4jfds 8932ds hisdf9f hs80823"

result = re.sub(r'\D', "", string1)
print(result)

result = re.sub(r'\D', " ", string1)
print(result)

result = re.sub(r'\D', ".", string1)
print(result)