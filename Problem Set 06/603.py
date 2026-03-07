n = int(input())
words = input().split()
result = []
for i, w in enumerate(words):
    result.append(str(i) + ":" + w)
print(" ".join(result))
