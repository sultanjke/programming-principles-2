import re

def double(match):
    return match.group() * 2

s = input()
result = re.sub(r'\d', double, s)
print(result)
