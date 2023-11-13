import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dp = [[0] * 201 for _ in range(201)]

for i in range(1, 201):
    dp[1][i] = i

for i in range(2, 201):
    dp[i][1] = 1
    for j in range(2, 201):
        dp[i][j] = dp[i][j-1] + dp[i-1][j]

print(dp[n][m] % 1000000000)
