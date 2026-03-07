import re

s = input()
p = input()
if re.search(re.escape(p), s):
    print("Yes")
else:
    print("No")
