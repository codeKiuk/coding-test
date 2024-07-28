def main():
    import sys
    from itertools import combinations
    input = sys.stdin.readline

    N, S = map(int, input().split())

    numbers = list(map(int, input().split()))
    answer = 0
    for i in range(1, N+1):
        combi_list = list(combinations(numbers, i))
        for combi in combi_list:
            if sum(combi) == S:
                answer += 1

    print(answer)
main()