import math
import random
import itertools

def is_prime_miller_rabin(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Write n-1 as 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    # Witness loop
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True

N = int(1e6)
primes = []
is_prime = [True for _ in range(N)]
is_prime[0] = False
is_prime[1] = False

for p in range(2, N):
    if not is_prime[p]:
        continue
    primes.append(p)
    for j in range(2 * p, N, p):
        is_prime[j] = False

ANS = set()

def parse(s):
    numbers = [int(x) for x in s.split("*")]
    numbers.sort()

    for e in numbers:
        if e < N and not is_prime[e]:
            return False
        if e >= N and not is_prime_miller_rabin(e):
            return False

    ANS.add(tuple(numbers))
    return True

def rec(curr, perm, index, n):
    if index == n:
        parse(curr)
        return

    if index < n - 1:
        rec(curr + str(perm[index]) + "*", perm, index + 1, n)

    rec(curr + str(perm[index]), perm, index + 1, n)

ANS = set()

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
perms = list(itertools.permutations(data))

for perm in perms:
    rec("", perm, 0, len(perm))

print("Sol", len(ANS))