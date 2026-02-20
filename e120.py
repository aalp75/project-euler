# rewriting (a - 1) ^ n + (a + 1) ^ n using binomial coefficient
# gives remainder of 2 when n is even and remainder of 2 * a * n when n is odd
# by pigeonhole principle at most a * a different values

N = 1000

ans = 0
for a in range(3, N + 1):
    if (a % 100 == 0):
        print(a)

    seen = set()
    mx = 2
    MOD = a * a

    for n in range(1, a * a + 1, 2):
        # print(n)
        r = 2 * a * n % MOD
        mx = max(mx, r)

    #print(a, mx)
    ans += mx

print(f'{ans:,}')