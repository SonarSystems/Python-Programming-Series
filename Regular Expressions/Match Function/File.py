import re

pattern = re.compile('ell')
print(pattern.match('hello world'))
print(pattern.match('hello world', 1))

result = pattern.match('hello world', 1)
