import re

pattern = r'[a-z]+ \d*'

string = 'hii 66 hello 33 something 4'
obj = re.findall(pattern, string)
if obj:
    print(obj)
else:
    print("no match found")
# find all retun in form of list
