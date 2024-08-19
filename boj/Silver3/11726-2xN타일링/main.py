import sys
def main():
    input = sys.stdin.readline

    N = int(input())

    dp = [0] * (N+1)
    dp[1] = 1
    if N == 1:
        print(dp[1])
        return
        
    dp[2] = 2

    if N >= 3:
        for i in range(3, N+1):
            dp[i] = (dp[i-1] + dp[i-2]) % 10007

    print(dp[N])

main()