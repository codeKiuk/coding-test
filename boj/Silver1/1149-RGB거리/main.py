import sys
def main():
    input = sys.stdin.readline
    N = int(input())
    houses = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] * 3 for _ in range(N+1)]
    
    dp[1][0] = houses[0][0]
    dp[1][1] = houses[0][1]
    dp[1][2] = houses[0][2]

    dp[2][0] = min(dp[1][1], dp[1][2]) + houses[1][0]
    dp[2][1] = min(dp[1][0], dp[1][2]) + houses[1][1]
    dp[2][2] = min(dp[1][0], dp[1][1]) + houses[1][2]

    for i in range(3, N+1):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + houses[i-1][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + houses[i-1][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + houses[i-1][2]

    print(min(dp[N])) 

main()