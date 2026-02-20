import math

TURN = 15

# dp[i][j] = probability to have i blues in j turns

dp = [[0.0 for _ in range(TURN + 1)] for _ in range(TURN + 1)]

dp[0][0] = 1

# dp[i][j] = dp[i][j - 1] * pick a red + dp[i - 1][j - 1] * pick a blue
for turn in range(1, TURN + 1):
    p = 1.0 / (turn + 1)  # proba to pick a blue
    q = 1.0 - p          # proba to pick a red

    dp[0][turn] = q * dp[0][turn - 1]

    for blue in range(1, TURN + 1):
        dp[blue][turn] = (
            dp[blue][turn - 1] * q
            + dp[blue - 1][turn - 1] * p
        )

ans = 0
for b in range(TURN // 2 + 1, TURN + 1):
    ans += dp[b][TURN]

print("ans:", math.floor(1 / ans))