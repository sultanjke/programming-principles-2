n = int(input())
first_entries = {}

for i in range(1, n + 1):
    s = input().strip()
    if s not in first_entries:
        first_entries[s] = i

sorted_keys = sorted(first_entries.keys())

for key in sorted_keys:
    print(key, first_entries[key])