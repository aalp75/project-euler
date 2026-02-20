# dp[i][j] = number of block fulfilling a bar of length i
# with the last block black (j = 0) and red (j = 1)

n = 50

dp = [[0 for _ in range(2)] for _ in range(n + 1)]

dp[0][0] = 1
dp[1][0] = 1

for i in range(2, n + 1):
    dp[i][0] = dp[i - 1][0] + dp[i - 1][1]

    for j in range(0, i - 2):
        dp[i][1] += dp[j][0]

ans = dp[n][0] + dp[n][1]

print(f"Solution: {ans:,}")