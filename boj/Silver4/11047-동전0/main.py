import sys
def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    coins = [int(input()) for _ in range(N)]
    answer = 0
    for i in range(N-1, -1, -1):
        count = K // coins[i]
        if count > 0:
            answer += count
            K -= count * coins[i]

    print(answer)

main()