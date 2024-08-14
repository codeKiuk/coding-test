import sys
def main():
    input = sys.stdin.readline
    N = int(input())
    stairs = [int(input()) for _ in range(N)]
    dp = [[0] * 3 for _ in range(301)] 
    dp[1][1] = stairs[0]
    dp[1][2] = 0
    if N == 1:
        print(dp[1][1])
        return
    dp[2][1] = stairs[1]
    dp[2][2] = stairs[0] + stairs[1]


    for i in range(3, N+1):
        dp[i][1] = max(dp[i-2][1], dp[i-2][2]) + stairs[i-1]
        dp[i][2] = dp[i-1][1] + stairs[i-1]
    print(max(dp[N][1], dp[N][2]))

        

main()