x = int(input())
num = list(map(int, input().split()))
maxval = max(num)
minval = min(num)

for i in range(x):
    if num[i] == maxval:
        num[i] = minval
print(*(num))

