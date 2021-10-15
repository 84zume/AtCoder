import re
a = str(input())

if(re.match("[A-Z]", a)):
    print("A")
else:
    print("a")
