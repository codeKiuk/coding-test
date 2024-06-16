def main2():
    # 시간초과!
    node, edge = map(int, input().split())
    graph = [[0] * (node + 1) for _ in range(node + 1)]
    visited = [False] * (node + 1)
    count = 0

    for i in range(edge):
        n, m = map(int, input().split())
        graph[n][m] = 1
        graph[m][n] = 1
        pass

    from collections import deque
    def bfs(v):
        queue = deque([v])
        while len(queue) > 0:
            current = queue.popleft()
            visited[current] = True
            for j, value in enumerate(graph[current]):
                if value == 1 and not visited[j] and j not in queue:
                    queue.append(j)

        pass

    for i in range(1, node + 1):
        if visited[i]:
            continue
        bfs(i)
        count += 1

    print(count)
    pass


def main():
    # 2차원배열말고, 2차원 인접 리스트로 풀기..?
    from collections import deque
    
    node, edge = map(int, input().split())
    count = 0
    graph = [[] for _ in range(node)]
    visited = [False] * (node)

    for i in range(edge):
        n, m = map(int, input().split())
        graph[n-1].append(m-1)
        pass

    def bfs(v):
        queue = deque([v])
        while len(queue) > 0:
            current = queue.popleft()
            visited[current-1] = True
            for j, value in enumerate(graph[current-1]):
                if not visited[j] and (j+1) not in queue:
                    queue.append((j+1))

        pass
    
    
    for i, value in enumerate(graph):
        print('visited:', visited)
        if visited[i]:
            continue
        bfs(i+1)
        count += 1
    print(count)
    pass

main()