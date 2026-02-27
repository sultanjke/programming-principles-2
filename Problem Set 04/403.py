import sys

def divisible_generator(n):
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

def main():
    line = sys.stdin.readline()
    if not line:
        return

    try:
        n = int(line.strip())
        gen = divisible_generator(n)

        try:
            first = next(gen)
            print(first, end='')
        except StopIteration:
            return

        for num in gen:
            print(f" {num}", end='')
        print()

    except ValueError:
        pass

if __name__ == "__main__":
    main()