import sys
def main():
    input = sys.stdin.readline
    N = int(input())
    count = 0
    
    dp = [0] * (N+1)

    for i in range(N+1):
        if i == 0:
            continue
        elif i == 1:
            dp[i] = 0
            continue

        if i % 6 == 0:
            dp[i] = min(dp[i//3], dp[i//2], dp[i-1]) + 1
        elif i % 3 == 0:
            dp[i] = min(dp[i//3], dp[i-1]) + 1
        elif i % 2 == 0:
            dp[i] = min(dp[i//2], dp[i-1]) + 1
        else:
            dp[i] = dp[i-1] + 1

    print(dp[N])

main()

# 17 16 8 4 2 1
# 17 16 15 5 4 3 1
# 17  3  1