import sys
from itertools import permutations
from collections import deque

def main():
    input = sys.stdin.readline

    N = int(input())
    numbers = list(map(int, input().split()))
    operators = list(map(int, input().split()))
    operator_permutations = []

    for idx, operator in enumerate(operators):
        operator_permutations += [idx] * operator

    operator_permutations = permutations(operator_permutations, N-1)

    max_answer = float('-inf')
    min_answer = float('inf')

    def get_result(operator_permutation, permu_idx, number, result):
        # print(f"number: {number}, result: {result}, permu_idx: {permu_idx}")
        if operator_permutation[permu_idx] == 0:
            result = number + result
        elif operator_permutation[permu_idx] == 1:
            result = result - number
        elif operator_permutation[permu_idx] == 2:
            result = number * result
        elif operator_permutation[permu_idx] == 3:
            if result == 0:
                result = 0
                return result
            elif result < 0:
                result = -(-result // number)
            else:
                result = result // number
        return result
    
    for operator_permutation in operator_permutations:
        # print(f"operator_permutation: {operator_permutation}")
        stack = deque([])
        result = 0
        permu_idx = 0
        for idx, number in enumerate(numbers):
            # print(f"permu_idx: {permu_idx}")
            if len(stack) == 0:
                stack.append(number)
                if idx == 0:
                    continue
            popped = stack.pop()
            if idx == 1:
                result += popped
                result = get_result(operator_permutation, permu_idx, number, result)
            else:
                result = get_result(operator_permutation, permu_idx, popped, result)
            # print(f"result: {result}")
            permu_idx += 1
        
        if len(stack) > 0:
            popped = stack.pop()
            result = get_result(operator_permutation, permu_idx, popped, result)
            # print(f"result: {result}")

        max_answer = max(max_answer, result)
        min_answer = min(min_answer, result)

    print(max_answer)
    print(min_answer)

main()

"""
operator permuations 을 구한다.
0 덧셈 1 뺄셈 2 곱셈 3 나눗셈
[0, 0, 0, 1, 2, 2, 3] N-1개
numbers
[0, 0, 0, 0, 0, 0, 0, 0] N개 짝수개

[0, 0, 0, 1, 2, 2] N-1개
[0, 0, 0, 0, 0, 0, 0] N개 홀수개

1 3 0 0 2 max
0 0 3 1 2 min
"""