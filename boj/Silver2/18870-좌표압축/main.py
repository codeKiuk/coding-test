import sys
from bisect import bisect_left
def main():
    input = sys.stdin. readline
    N = int(input())
    numbers = list(map(int, input().split()))

    sorted_numbers = sorted(set(numbers))
    count_dict = {}
    
    for num in sorted_numbers:
        count_dict[num] = bisect_left(sorted_numbers, num)

    for num in numbers:
        print(f"{count_dict[num]}", end=' ')

main()