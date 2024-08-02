import sys
from itertools import combinations_with_replacement
from bisect import bisect_left
def main():
    input = sys.stdin.readline

    N = int(input())
    U = sorted([int(input()) for _ in range(N)])
    combination_list = list(combinations_with_replacement(U, 2))
    max_value = float('-inf')
    sum_list = sorted([sum(combi) for combi in combination_list])

    for i in U:
        for j in U:
            target = j - i
            target_idx = bisect_left(sum_list, target)
            if sum_list[target_idx] != target:
                continue
            max_value = max(max_value, j)

    print(max_value)


main()