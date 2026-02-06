n = int(input())
numbers = list(map(int, input().split()))

max_val = numbers[0]
pos = 1

for i in range(1, n):
    if numbers[i] > max_val:
        max_val = numbers[i]
        pos = i + 1

print(pos)
