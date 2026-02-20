# dp[i] = number of ways to fill a bar of length i

n = 50
ans = 0

dp = [0 for _ in range(n + 1)]
dp[0] = 1

for i in range(1, n + 1):
    dp[i] = dp[i - 1]  # black block

    for length in [2, 3, 4]:
        if i - length >= 0:
            dp[i] += dp[i - length]

ans = dp[n]

print(f"Solution: {ans:,}")