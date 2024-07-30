import sys
def main():
    input = sys.stdin.readline

    N, M = map(int, input().split())

    sorted_N_list = sorted([str(input()) for _ in range(N)])
    sorted_M_list = sorted([str(input()) for _ in range(M)])

    answer_list = []

    def binary_search(name, sorted_list, left, right):
        if left > right:
            return False

        mid = (left + right) // 2
        mid_val = sorted_list[mid]

        if name == mid_val:
            return True
        elif name > mid_val:
            return binary_search(name, sorted_list, mid+1, right)
        else:
            return binary_search(name, sorted_list, left, mid-1)

    for m in sorted_M_list:
        is_in_N = binary_search(m, sorted_N_list, 0, N-1)
        if is_in_N:
            answer_list.append(m)

    print(len(answer_list))
    for answer in answer_list:
        print(answer.strip())

main()