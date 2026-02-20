import copy

N = 5000
MX = 1548136 + 10  # sum of all primes up to 5,000
primes = []
is_prime = [True] * MX

for i in range(2, MX):
    if not is_prime[i]:
        continue

    primes.append(i)
    for j in range(2 * i, MX, i):
        is_prime[j] = False

n = len(primes)

dp = [0] * MX
dp[0] = 1

MOD = 10 ** 16

for p in primes:
    if p > N:
        break

    dp_next = copy.deepcopy(dp)

    for j in range(MX):
        if dp[j] == 0:
            continue

        dp_next[j + p] += dp[j]
        if dp_next[j + p] >= MOD:  # fast modulo
            dp_next[j + p] -= MOD

    dp = dp_next

ans = 0
for p in primes:
    ans = ans + dp[p]

print(f'{ans % MOD:,}')