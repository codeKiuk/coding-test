def main():
    import sys
    input = sys.stdin.readline

    N = int(input())

    import heapq
    import math
    array =  []
    heapq.heapify(array)

    for _ in range(N):
        for item in list(map(int, input().split())):
            if len(array) < N:
                heapq.heappush(array, item)
            else:
                heapq.heappushpop(array, item)

    large_elements = heapq.nlargest(N, array)
    print(large_elements[N-1])



main()