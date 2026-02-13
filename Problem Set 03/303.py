def letters_to_number(s):
    d = {
        "ZER": "0",
        "ONE": "1",
        "TWO": "2",
        "THR": "3",
        "FOU": "4",
        "FIV": "5",
        "SIX": "6",
        "SEV": "7",
        "EIG": "8",
        "NIN": "9"
    }
    num = ""
    for i in range(0, len(s), 3):
        part = s[i:i+3]
        num += d[part]
    return int(num)

def number_to_letters(n):
    d = {
        "0": "ZER",
        "1": "ONE",
        "2": "TWO",
        "3": "THR",
        "4": "FOU",
        "5": "FIV",
        "6": "SIX",
        "7": "SEV",
        "8": "EIG",
        "9": "NIN"
    }
    result = ""
    for digit in str(n):
        result += d[digit]
    return result

s = input()

for i in range(len(s)):
    if s[i] in "+-*":
        op = s[i]
        left = s[:i]
        right = s[i+1:]
        break

a = letters_to_number(left)
b = letters_to_number(right)

if op == "+":
    res = a + b
elif op == "-":
    res = a - b
else:
    res = a * b

print(number_to_letters(res))
