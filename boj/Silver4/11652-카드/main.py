import sys
from collections import Counter
def main():
    input = sys.stdin.readline

    N = int(input())
    numbers = [int(input()) for _ in range(N)]
    counter = Counter(numbers)

    max_count = float('-inf')
    answer = float('inf')

    for key, count in counter.items():
        if count > max_count:
            max_count = count
            answer = key
        elif count == max_count:
            answer = min(answer, key)

    print(answer)   
main()