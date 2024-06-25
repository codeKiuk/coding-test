def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    graph = [list(map(int, input().strip())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    # graph = [list(input()) for _ in range(n)]
    # graph = [[int(j) for j in i[:-1]] for i in graph]

    #     좌 우  하  상
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    all_group_count = 0
    group_count_list = []

    def bfs(v):
        from collections import deque
        queue = deque([v])
        group_count = 1

        while queue:
            x, y = queue.popleft()
            visited[x][y] = True

            for i in range(4):
                target_x = x + dx[i]
                target_y = y + dy[i]

                if target_x >= 0 and target_y >= 0 and target_x < n and target_y < n and not visited[target_x][target_y] and graph[target_x][target_y] == 1 and (target_x, target_y) not in queue:
                    group_count += 1
                    queue.append((target_x, target_y))
                    visited[target_x][target_y] = True

        group_count_list.append(group_count)

    for i, inner_list in enumerate(graph):
        for j, value in enumerate(inner_list):
            if visited[i][j] or value == 0:
                continue
            bfs((i, j))
            all_group_count += 1

    print(all_group_count)
    group_count_list.sort()
    for i in group_count_list:
        print(i)
    pass

main()