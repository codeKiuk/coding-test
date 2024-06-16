def main():
    # 4 5 1
    # 1 2
    # 1 3
    # 1 4
    # 2 4
    # 3 4

    from collections import deque

    node, edge, start = map(int, input().split())
    graph = [[0] * node for _ in range(node)]

    for i in range(edge):
        from_node, to_node = map(int, input().split())

        graph[from_node - 1][to_node - 1] = 1
        graph[to_node - 1][from_node - 1] = 1

    dfs_result = []
    bfs_result = []

    visited = [False] * node
    def dfs(visited, v, graph):
        visited[v-1] = True
        dfs_result.append(v)
        for i, value in enumerate(graph[v-1]):
            if value == 1 and not visited[i]:
                # 아니 첨에 여기서 return dfs 했는데.. 리턴을 해버리면 그 다음 루프를 안 돌잖아!!!!!!!!
                #  난 바보야....멍청이...
                dfs(visited, i+1, graph)

    
    dfs(visited, start, graph)
    print(' '.join(map(str, dfs_result)))
    
    
    def bfs():
        visited = [False] * node
        queue = deque([start])
    
        while len(queue) > 0:
            current = queue.popleft()
            visited[current-1] = True
            bfs_result.append(current)

            for i, value in enumerate(graph[current-1]):
                if value == 1 and not visited[i] and i+1 not in queue:
                    queue.append(i+1)


        print(' '.join(map(str, bfs_result)))
        pass

    
    bfs()
    pass

main()