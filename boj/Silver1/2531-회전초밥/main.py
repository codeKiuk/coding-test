import sys
def main():
    input = sys.stdin.readline
    N, d, k, c = map(int, input().split())
    sushi_list = [int(input()) for _ in range(N)]

    start = 0
    end = k
    max_sushi_category = float('-inf')

    while start < N:
        if end <= N:
            sushi_counter = set(sushi_list[start:end])
        else:
            tmp_end = end - N
            sushi_counter = set(sushi_list[start:] + sushi_list[:tmp_end])
        is_c_in_sushi = c in sushi_counter
        max_sushi_category = max(max_sushi_category, len(sushi_counter) if is_c_in_sushi else len(sushi_counter)+1)

        start += 1
        end += 1

    print(max_sushi_category)
        


main()