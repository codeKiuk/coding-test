def main():
    node = int(input())
    edge = int(input())

    graph = [[0] * (node + 1) for _ in range(node + 1)]
    visited = [False] * (node + 1) # 결국 True 개수를 출력하면 된다

    for i in range(edge):
        n, m = map(int, input().split())
        graph[n][m] = 1
        graph[m][n] = 1


    def bfs():
        from collections import deque
        queue = deque([1])

        while len(queue) > 0:
            current = queue.popleft()
            visited[current] = True
            
            for i,value in enumerate(graph[current]):
                if value == 1 and not visited[i] and i not in queue:
                    queue.append(i)

    bfs()
    print(visited.count(True) - 1)
    pass

main()