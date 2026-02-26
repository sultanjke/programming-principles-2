import json

def deep_diff(a, b, path=""):
    diffs = []
    all_keys = set()
    if isinstance(a, dict):
        all_keys.update(a.keys())
    if isinstance(b, dict):
        all_keys.update(b.keys())

    for key in all_keys:
        current_path = path + "." + key if path else key
        in_a = isinstance(a, dict) and key in a
        in_b = isinstance(b, dict) and key in b

        if not in_a:
            diffs.append(current_path + " : <missing> -> " + json.dumps(b[key], separators=(',', ':')))
        elif not in_b:
            diffs.append(current_path + " : " + json.dumps(a[key], separators=(',', ':')) + " -> <missing>")
        elif isinstance(a[key], dict) and isinstance(b[key], dict):
            diffs.extend(deep_diff(a[key], b[key], current_path))
        elif a[key] != b[key]:
            diffs.append(current_path + " : " + json.dumps(a[key], separators=(',', ':')) + " -> " + json.dumps(b[key], separators=(',', ':')))

    return diffs

a = json.loads(input())
b = json.loads(input())
diffs = deep_diff(a, b)
diffs.sort()
if diffs:
    for d in diffs:
        print(d)
else:
    print("No differences")
