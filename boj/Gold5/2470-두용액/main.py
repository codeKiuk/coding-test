import sys
def main():
    input = sys.stdin.readline

    N = int(input())
    numbers = sorted(list(map(int, input().split())))
    
    start = 0
    end = N - 1
    answer_idx = (start, end)
    min_num = abs(numbers[start] + numbers[end])
    if abs(numbers[start]) > abs(numbers[end]):
        start += 1
    else:
        end -= 1
    while start < end:
        target = abs(numbers[start] + numbers[end])
        if target <= min_num:
            min_num = target
            answer_idx = (start, end)
            if abs(numbers[start]) > abs(numbers[end]):
                start += 1
            else:
                end -= 1
        else:
            if abs(numbers[start]) > abs(numbers[end]):
                start += 1
            else:
                end -= 1


    print(f"{numbers[answer_idx[0]]} {numbers[answer_idx[1]]}")
main()

# -2 -1 99 1000 10000
# -99 -2 -1 9999 98888
# -100000 -10000 -9999 -11 0 1 2
# -101010 -10101 -999 1 2 10000 999999