import sys
def main():
    input = sys.stdin.readline
    N = int(input())
    dp = [0] * (10**6 + 1)
    tmp = [0] * (10**6 + 1)

    dp[1] = 0
    if N == 1:
        print(0)
        print(1)
        return
    
    for i in range(2, N+1):
        if i % 6 == 0:
            dp[i] = min(dp[i//3], dp[i//2], dp[i-1]) + 1
            if dp[i//3] <= dp[i//2] and dp[i//3] <= dp[i-1]:
                tmp[i] = "".join(f"{i//3} {tmp[i//3]}") 
            elif dp[i//2] <= dp[i//3] and dp[i//2] <= dp[i-1]:
                tmp[i] = "".join(f"{i//2} {tmp[i//2]}")
            else:
                tmp[i] = "".join(f"{i-1} {tmp[i-1]}")
        elif i % 2 == 0:
            dp[i] = min(dp[i//2], dp[i-1]) + 1
            if dp[i//2] <= dp[i-1]:
                tmp[i] = "".join(f"{i//2} {tmp[i//2]}")
            else:
                tmp[i] = "".join(f"{i-1} {tmp[i-1]}")
        elif i % 3 == 0:
            dp[i] = min(dp[i//3], dp[i-1]) + 1
            if dp[i//3] <= dp[i-1]:
                tmp[i] = "".join(f"{i//3} {tmp[i//3]}")
            else:
                tmp[i] = "".join(f"{i-1} {tmp[i-1]}")
        else:
            dp[i] = dp[i-1] + 1
            tmp[i] = "".join(f"{i-1} {tmp[i-1]}")

    print(dp[N])
    print("".join(f"{N} {''.join(tmp[N].split(' 0'))}"))

        

main()