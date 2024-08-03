import sys
from itertools import product
from bisect import bisect_left
from collections import defaultdict
# N 최대 4000 -> O(N**2) 가능
def main():
    input = sys.stdin.readline

    N = int(input())
    A = []
    B = []
    C = []
    D = []

    for _ in range(N):
        a, b, c, d = map(int, input().split())
        A.append(a)
        B.append(b)
        C.append(c)
        D.append(d)

    sum_CD_dict = defaultdict(int)

    for c in C:
        for d in D:
            sum_CD_dict[c+d] += 1


    answer = 0

    for a in A:
        for b in B:
            target = -(a+b)
            if target in sum_CD_dict:
                answer += sum_CD_dict[target]

    print(answer)

main()