# dp[i][j] = number of block fulfilling a bar of length i
# with the last block black (j = 0) and red (j = 1)

n = 50
ans = 0

for length in [2, 3, 4]:

    dp = [[0 for _ in range(2)] for _ in range(n + 1)]

    dp[0][0] = 1

    for i in range(1, n + 1):
        dp[i][0] = dp[i - 1][0] + dp[i - 1][1]

        if i - length >= 0:
            dp[i][1] = dp[i - length][0] + dp[i - length][1]

    ans += dp[n][0] + dp[n][1] - 1

print(f"Solution: {ans:,}")