n = 100

dp = [[0 for _ in range(10)] for _ in range(n + 1)]

for k in range(10):
    dp[1][k] = 1

ans1 = sum(dp[1][1:])
print(ans1)

for i in range(2, n + 1):
    for j in range(10):
        for k in range(j, 10):
            dp[i][j] += dp[i - 1][k]

    ans1 += sum(dp[i][1:])

print(f"ans 1 = {ans1:,}")

dp = [[0 for _ in range(10)] for _ in range(n + 1)]

for k in range(10):
    dp[1][k] = 1

ans2 = sum(dp[1][1:])

for i in range(2, n + 1):
    for j in range(10):
        for k in range(j, -1, -1):
            dp[i][j] += dp[i - 1][k]

    ans2 += sum(dp[i][1:])

print(f"ans 2 = {ans2:,}")

ans = ans1 + ans2 - 9 * n

print(f"Solution is {ans:,}")