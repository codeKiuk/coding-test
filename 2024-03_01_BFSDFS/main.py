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
        

solution1()