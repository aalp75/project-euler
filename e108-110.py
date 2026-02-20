primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
n = len(primes)

P = 3
ans = -1

lim = 4_000_000
#lim = 1000


def recurr(curr, index):
    global ans

    if index == n:
        v = 1
        vs = 1
        div = 1

        for prime, exp in curr:
            v *= prime ** exp
            vs *= prime ** (2 * exp)
            div *= (2 * exp + 1)

        if v == 9350130049860600:
            print(curr)

        if div > 2 * lim:
            ans = v if ans == -1 else min(ans, v)

        return

    for p in range(P + 1):
        curr.append((primes[index], p))
        recurr(curr, index + 1)
        curr.pop()


start = []
recurr(start, 0)

print(f"{ans:,}")