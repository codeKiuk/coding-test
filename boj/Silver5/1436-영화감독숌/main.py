def main():
    import sys
    input = sys.stdin.readline

    max_number = 3000000

    # 적어도 6이 3개 이상 연속-포함되어있는 숫자

    n = int(input())

    target_numbers = []

    for i in range(1, max_number+1):
        num_to_str = str(i)
        if '666' in num_to_str:
            target_numbers.append(i)
            


    print(target_numbers[n-1])



main()