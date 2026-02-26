def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def primes(n):
    for num in range(2, n + 1):
        if is_prime(num):
            yield num

n = int(input())
result = list(primes(n))
if result:
    print(" ".join(str(x) for x in result))
