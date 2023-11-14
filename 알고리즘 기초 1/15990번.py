input = sys.stdin.readline

dp = [[0 for _ in range(3)] for _ in range(100001)]

# n이 1일때 2일때 3일때 각각 1,2,3으로 끝나는 상황의 개수 초기화
dp[1] = [1, 0, 0]
dp[2] = [0, 1, 0]
dp[3] = [1, 1, 1]

for i in range(4, 100001):
    # 1로 끝나는 경우, 1을 뺀 값의 2와 3으로 끝나는 개수를 더한다
    dp[i][0] = (dp[i - 1][1] + dp[i - 1][2]) % 1000000009
    # 2로 끝나는 경우, 2를 뺀 값의 1과 3으로 끝나는 개수를 더한다
    dp[i][1] = (dp[i - 2][0] + dp[i - 2][2]) % 1000000009
    # 3으로 끝나는 경우, 3을 뺀 값의 1과 2로 끝나는 개수를 더한다
    dp[i][2] = (dp[i - 3][0] + dp[i - 3][1]) % 1000000009

T = int(input())
for i in range(T):
    n = int(input())
    print(sum(dp[n]) % 1000000009)
