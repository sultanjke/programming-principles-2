import sys

class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

def main():
    line = sys.stdin.read().strip()
    if not line:
        return

    rev_iter = Reverse(line)
    for char in rev_iter:
        print(char, end='')
    print()

if __name__ == "__main__":
    main()