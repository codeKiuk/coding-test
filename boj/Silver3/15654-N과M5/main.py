import sys
def main():
    from itertools import permutations
    input = sys.stdin.readline
    N, M = map(int, input().split())
    array = sorted(list(map(int, input().split())))
    product_array = list(permutations(array, M))

    for p in product_array:
        print(*p)

main()