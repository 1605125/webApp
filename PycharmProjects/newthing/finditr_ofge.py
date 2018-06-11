import re

pattern = r'[a-z]+ \d*'

string = 'hii 66 hello 33 something 4'
obj = re.finditer(pattern, string)
if obj:
    # print(obj)
    for match in obj:
        print(match.group())
else:
    print("no match found")

