def main():
    import sys
    input = sys.stdin.readline

    N, M = map(int, input().split())

    from itertools import permutations

    result = list(permutations(range(1, N+1), M))

    for item in result:
        print(' '.join(map(str, item)))


main()