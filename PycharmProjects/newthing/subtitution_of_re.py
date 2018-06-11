import re

pattern = r'\s'

string = 'hii 66 hello 33 something 4'
# obj = re.sub(pattern, '_', string)
obj = re.subn(pattern, '_', string) # how many times string has been replaced
if obj:
    print(obj)
else:
    print("no match found")
