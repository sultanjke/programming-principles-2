import sys

def even_generator(n):
    for i in range(0, n + 1, 2):
        yield i

def main():
    line = sys.stdin.readline()
    if not line:
        return

    try:
        n = int(line.strip())
        gen = even_generator(n)

        try:
            first = next(gen)
            print(first, end='')
        except StopIteration:
            return

        for even in gen:
            print(f",{even}", end='')
        print() 

    except ValueError:
        pass

if __name__ == "__main__":
    main()