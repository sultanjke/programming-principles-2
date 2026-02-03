n = int(input())

nums = input().split()

max = int(nums[0])

for x in nums:
    x = int(x)
    if x > max:
        max = x

print(max)
