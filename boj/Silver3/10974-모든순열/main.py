def main():
    import sys
    from itertools import permutations
    input = sys.stdin.readline

    N = int(input())

    for item in  list(permutations(range(1, N+1))):
        print(" ".join(map(str, item)))

main()