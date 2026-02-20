# dynamic programming to compute all subset possible sums

import copy

def fast_exponentiation_mod(base: int, exponent: int, mod: int) -> int:
    result = 1
    base = base % mod
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exponent //= 2
    return result


N = 250250
d = 250

dp = [0] * d
dp[0] = 1

MOD = 10 ** 16

for i in range(1, N + 1):
    x = fast_exponentiation_mod(i, i, d)
    dp_next = copy.deepcopy(dp)

    for j in range(d):
        dp_next[(j + x) % d] += dp[j]
        dp_next[(j + x) % d] %= MOD

    dp = dp_next

print(f'{dp[0] - 1:,}')