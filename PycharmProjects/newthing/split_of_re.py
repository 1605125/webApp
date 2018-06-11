import re

pattern = r'\s'

string = 'hii 66 hello 33 something 4'
obj = re.split(pattern, string)
if obj:
    print(obj)
else:
    print("no match found")
