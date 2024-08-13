import sys
def main():
    input = sys.stdin.readline
    T = int(input())
    test_cases = [int(input()) for _ in range(T)]

    dp = [0] * 12
    
    for n in range(12):
        if n == 1:
            dp[1] = 1
        elif n == 2:
            dp[2] = 2
        elif n == 3:
            dp[3] = 4
        else:
            dp[n] = dp[n-1] + dp[n-2] + dp[n-3]

    for case in test_cases:
        print(dp[case])
        



main()