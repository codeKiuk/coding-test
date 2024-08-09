import sys
def main():
    input = sys.stdin.readline
    N = int(input())
    kg_list = sorted([int(input()) for _ in range(N)])
    max_weight = float('-inf')
    for idx, weight in enumerate(kg_list):
        max_weight = max(max_weight,weight * (N - idx))

    print(max_weight)


main()