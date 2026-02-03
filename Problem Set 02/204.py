n = int(input())

nums = input().split()

count = 0

for x in nums:
    if int(x) > 0:
        count += 1

print(count)