
def main():
    import sys
    from itertools import product
    input = sys.stdin.readline

    # 비밀번호 길이, 알고있는 비밀번호 수
    N, M = map(int, input().split())
    numbers = []
    if M == 0:
        pass
    else:
        numbers = list(map(int, input().split()))

    answer = 0

    permutation_list = product(range(0, 10), repeat=N)

    for permutation in permutation_list:
        is_valid = True
        for number in numbers:
            if number not in permutation:
                is_valid = False
                break
        if is_valid:
            answer += 1

    print(answer)
        

main()