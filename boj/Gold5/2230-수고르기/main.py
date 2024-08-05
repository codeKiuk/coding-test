import sys
from bisect import bisect_left
def main():
    input = sys.stdin.readline

    N, M = map(int, input().split())
    A = sorted([int(input()) for _ in range(N)])
    min_diff = float('inf')

    for i in A:
        target = i + M
        target_idx = bisect_left(A, target)
        target_idx = target_idx if target_idx < N else N - 1
        diff = A[target_idx] - i
        if diff < M:
            continue
        min_diff = min(min_diff, diff)

    print(min_diff)

main()