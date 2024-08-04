import sys
def main():
    input = sys.stdin.readline

    K, N = map(int, input().split())
    lan_list = sorted([int(input()) for _ in range(K)])
    max_lan_length = lan_list[-1]
    min_lan_length = 1

    def get_lan_count(length):
        return sum([lan // length for lan in lan_list])

    answer = float('-inf')
    
    while min_lan_length <= max_lan_length:
        mid = (min_lan_length + max_lan_length) // 2
        mid_lan_count = get_lan_count(mid)

        if mid_lan_count < N:
            max_lan_length = mid - 1
        elif mid_lan_count >= N:
            answer = max(answer, mid)
            min_lan_length = mid + 1


    print(answer)

main()
