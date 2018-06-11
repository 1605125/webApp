import re

pattern = r'[^@ ]+@[^@]+\.[^@]{3}'
string = 'syz@gmail.com abc@gmail.com Raj@gmail manas@gmail.com'
obj = re.findall(pattern, string)
if obj:
    print(obj)
else:
    print("no match found")