import sys

def recursion_solution():
    input = sys.stdin.readline
    N, S = map(int, input().split())
    numbers = list(map(int, input().split()))
    answer = 0

    def recursion(length, nodes, idx=0):
        nonlocal answer
        nonlocal S
        nonlocal N
        nonlocal numbers

        if len(nodes) == length:
            if sum(nodes) == S:
                answer += 1
            return

        if idx == N:
            return

        for index in range(idx, N):
            node = numbers[index]
            nodes.append(node)
            recursion(length, nodes, index+1)
            nodes.pop()

    for i in range(1, N+1):
        recursion(i, [])

    print(answer)

recursion_solution()

from itertools import combinations
def main():
    input = sys.stdin.readline

    N, S = map(int, input().split())

    numbers = list(map(int, input().split()))
    answer = 0
    for i in range(1, N+1):
        combi_list = list(combinations(numbers, i))
        for combi in combi_list:
            if sum(combi) == S:
                answer += 1

    print(answer)