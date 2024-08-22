import sys, heapq
def main():
    input = sys.stdin.readline
    N = int(input())
    M = int(input())
    d = [[] for _ in range(N+1)]
    for route in range(M):
        start, end, cost = map(int, input().split())
        d[start].append((start, end, cost))

    target_start, target_end = map(int, input().split())

    d_result = [float('inf') for _ in range(N+1)]
    d_result[target_start] = 0
    route_table = [-1] * (N+1)
    heap = []
    heapq.heapify(heap)
    
    # 시작점 힙에 추가
    heapq.heappush(heap, (0, target_start))

    while heap:
        weight, start = heapq.heappop(heap)
        if d_result[start] < weight:
            continue

        for next_vertex in d[start]:
            start, end, cost = next_vertex
            if d_result[end] > weight + cost:
                d_result[end] = weight + cost
                heapq.heappush(heap, (weight + cost, end))
                route_table[end] = start

    print(d_result[target_end])
    target_route = route_table[target_end]
    result_route = [target_end]
    while target_route != -1:
        result_route.append(target_route)
        target_route = route_table[target_route]

    print(len(result_route))
    print(*result_route[::-1])


main()