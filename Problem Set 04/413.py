import json

def resolve(data, query):
    parts = []
    current = ""
    i = 0
    while i < len(query):
        if query[i] == '.':
            if current:
                parts.append(current)
                current = ""
        elif query[i] == '[':
            if current:
                parts.append(current)
                current = ""
            j = i + 1
            while j < len(query) and query[j] != ']':
                j += 1
            parts.append(int(query[i+1:j]))
            i = j
        else:
            current += query[i]
        i += 1
    if current:
        parts.append(current)

    result = data
    for part in parts:
        try:
            if isinstance(part, int):
                result = result[part]
            else:
                result = result[part]
        except (KeyError, IndexError, TypeError):
            return "NOT_FOUND"
    return json.dumps(result, separators=(',', ':'))

data = json.loads(input())
q = int(input())
for _ in range(q):
    query = input()
    print(resolve(data, query))
