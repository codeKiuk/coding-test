import sys
def main():
    input = sys.stdin.readline
    N = int(input())
    A = sorted(list(map(int, input().split())), reverse=True)
    B = sorted(list(map(int, input().split())))
    result = 0
    for i in range(N):
        result += A[i] * B[i]

    print(result)

main()