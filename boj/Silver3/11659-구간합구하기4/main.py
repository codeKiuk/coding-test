import sys
def main():
    input = sys.stdin.readline

    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    sum_list = []
    results = []

    for idx in range(N):
        if idx == 0:
            sum_list.append(numbers[idx])
        else:
            sum_list.append(sum_list[idx-1] + numbers[idx])

    for _ in range(M):
        start, end = map(int, input().split())
        start -= 1
        end -= 1

        if start == 0:
            results.append(sum_list[end])

        else:
            results.append(sum_list[end] - sum_list[start-1])

    for result in results:
        print(result)
main()