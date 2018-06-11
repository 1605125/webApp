import re

pattern = r'[a-z]+ \d*'

string = 'hii 66 hello 33 something 4'
# obj = re.match(pattern, string)
obj = re.search(pattern, string)
if obj:
    print(obj.group())
else:
    print("no match found")
