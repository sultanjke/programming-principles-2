n = int(input())
surnames = set()

for i in range(n):
    name = input().strip()
    surnames.add(name)

print(len(surnames))