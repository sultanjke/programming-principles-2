n, l, r = map(int, input().split())
a = list(map(int, input().split()))

sub = a[l-1:r]
a[l-1:r] = sub[::-1]

print(*(a))