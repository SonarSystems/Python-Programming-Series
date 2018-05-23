import re

pattern = re.compile('ell')
print(pattern.match('hello world'))
print(pattern.match('hello world', 1))

print(pattern.search('hello world'))
print(pattern.search('hello world', 1))
print(pattern.search('hello world', 2))