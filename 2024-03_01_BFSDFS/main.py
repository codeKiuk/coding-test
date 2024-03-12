# 음료수 얼려 먹기 문제 
# N M
# N만큼 배열 입력 또 받는다.
def solution1():
    n, m = map(int, input().split())
    graph = []
    ice_group_count = 0
    visited = [[False] * m for _ in range(n)]

    # graph 입력 받기
    for i in range(n):
        input_string = input() # 0110111 이런식으로 입력 받는다.
        m_array = [int(x) for x in input_string]
        graph.append(m_array)


    def dfs(graph, v, visited):
        [i, j] = v

        if i < 0 or i >= n or j < 0 or j >= m: 
            return False
        if not visited[i][j] and graph[i][j] == 0:
            visited[i][j] = True
            dfs(graph, [i-1, j], visited)
            dfs(graph, [i+1, j], visited)
            dfs(graph, [i, j-1], visited)
            dfs(graph, [i, j+1], visited)
            return True
        return False

    for i, arr in enumerate(graph):
        for j, value in enumerate(arr):
            if dfs(graph, [i, j], visited) == True:
                ice_group_count += 1

    print("RESULT: ", ice_group_count)
        

# 미로 탈출
# 괴물이 있는 부분은 0, 없는 부분은 1
# 미로 탈출의 최소 칸 개수를 세면 된다
# n,m 까지 이동하는 최소 칸의 개수
def solution2():
    # N*M
    from collections import deque

    n, m = map(int, input().split())

    graph = []

    # graph 입력 받기
    for i in range(n):
        # 010111 이런식으로 입력 받는다.
        graph.append(list(map(int, input())))

    print("graph: ", graph)

    result = 0
    column = 0
    for i, _value in enumerate(graph):
        print(f"i: {i}, column: {column}")
        for j in range(column, m):
            if graph[i][j] == 1:
                graph[i][j] = 0 # visited 처리
                column = j
                result += 1
                print("colum, result: ", column," " ,result)
            else:
                break

    print("result: ", result)

    pass

# 미로 탈출 문제 정석 BFS로 풀면?
def solution3():
    from collections import deque

    n, m = map(int, input().split())

    graph = []

    # graph 입력 받기
    for i in range(n):
        # 010111 이런식으로 입력 받는다.
        graph.append(list(map(int, input())))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))

        while queue:
            (x, y) = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if graph[nx][ny] == 0:
                    continue
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))

        return graph[n-1][m-1]
    
    print(bfs(0, 0))
    
    
solution3()