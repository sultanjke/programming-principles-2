import importlib

q = int(input())
for _ in range(q):
    parts = input().split()
    module_path = parts[0]
    attr_name = parts[1]

    try:
        mod = importlib.import_module(module_path)
    except Exception:
        print("MODULE_NOT_FOUND")
        continue

    if not hasattr(mod, attr_name):
        print("ATTRIBUTE_NOT_FOUND")
    elif callable(getattr(mod, attr_name)):
        print("CALLABLE")
    else:
        print("VALUE")
