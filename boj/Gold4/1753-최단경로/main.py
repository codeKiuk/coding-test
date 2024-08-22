import sys
import heapq
def main():
    input = sys.stdin.readline
    V, E = map(int, input().split())
    K = int(input())

    d = [[] for _ in range(V+1)] 
    for _ in range(E):
        u, v, w = map(int, input().split())
        d[u].append((u, v, w))

    heap = []
    heapq.heapify(heap)
    d_result = [float('inf') for _ in range(V+1)]
    d_result[K] = 0

    # 시작점 추가
    heapq.heappush(heap, (0, K))

    while heap:
        w, u = heapq.heappop(heap)
        if d_result[u] < w:
            continue

        for next_vertex in d[u]:
            next_u, next_v, next_w = next_vertex
            next_weight = next_w + d_result[u]
            if next_weight < d_result[next_v]:
                heapq.heappush(heap, (next_weight, next_v))
                d_result[next_v] = next_weight

    for result in d_result[1:]:
        if result == float('inf'):
            print('INF')
        else:
            print(result)


main()

"""
1 -> 2 : 2
1 -> 3 : 3
2 -> 3 : 4
2 -> 4 : 5
3 -> 4 : 6
5 -> 1 : 1

"""