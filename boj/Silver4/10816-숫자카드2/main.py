import sys
from bisect import bisect_left, bisect_right
def main():
    input = sys.stdin.readline

    N = int(input())
    cards = sorted(list(map(int, input().split())))
    M = int(input())
    targets = list(map(int, input().split()))

    for target in targets:
        left_most_idx = bisect_left(cards, target)
        right_most_idx = bisect_right(cards, target)

        if left_most_idx == -1:
            print(0, end=' ')
        else:
            print(f"{right_most_idx - left_most_idx}", end=' ')
        

main()