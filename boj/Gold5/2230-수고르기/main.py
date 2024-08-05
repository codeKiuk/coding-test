import sys
from bisect import bisect_left
def main(): # 이분탐색 풀이
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


def main2(): # 투포인터 풀이# 투포인터 풀이
    input = sys.stdin.readline

    N, M = map(int, input().split())
    A = sorted([int(input()) for _ in range(N)])
    min_diff = float('inf')

    start_idx = 0
    end_idx = 0

    while end_idx < N and start_idx < N:
        diff = A[end_idx] - A[start_idx]
        if diff < M:
            end_idx += 1
        else:
            min_diff = min(min_diff, diff)
            start_idx += 1

    print(min_diff)


main2()