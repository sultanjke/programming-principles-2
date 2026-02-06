n = int(input())
a = list(map(int, input().split()))
a.sort()

best_val = a[0]
max_cnt = 0

curr_cnt = 0
for i in range(n):
    curr_cnt += 1
    if i == n - 1 or a[i] != a[i+1]:
        if curr_cnt > max_cnt:
            max_cnt = curr_cnt
            best_val = a[i]
        curr_cnt = 0

print(best_val)