def cycle(lst, k):
    for i in range(k):
        for item in lst:
            yield item

items = input().split()
k = int(input())
print(" ".join(str(x) for x in cycle(items, k)))
