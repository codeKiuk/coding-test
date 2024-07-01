# dfs+백트래킹 한계 : 최단경로인지 아닌지 판단불가 / 깊이우선 및 백트래킹으로 도달경로가 있는지, 없는지는 판단 가능하지만..
def main2():
    import sys
    input = sys.stdin.readline

    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]

    n, m = map(int, input().split())
    graph = [list(map(int, input().strip())) for _ in range(n)]
    visited = [[False]*m for _ in range(n)]

    start_node = (0, 0)
    max_wall = 1

    def dfs(v, max_wall, count, back_nodes=[], back_flag=False):
        x, y = v
        visited[x][y] = True
        None if back_flag else back_nodes.append(v)
        print("(x,y):({},{}), count: {}, max_wall: {}, back?: {}".format(x, y, count, max_wall, back_flag))

        if x == n-1 and y == m-1:
            print(count)
            return count

        # 종료조건
        if max_wall == 0:
            can_go_list = [False] * 4
            for i in range(4):
                next = (x + dx[i], y + dy[i])
                X, Y = next

                if 0 <= X <= n-1 and 0 <= Y <= m-1 and not visited[X][Y] and graph[X][Y] == 0:
                    can_go_list[i] = True
            can_go = True if True in can_go_list else False
            if can_go:
                pass
            else:
                # 아까 왔던 데로 가야제..
                if count == 1:
                    return -1
                back_max_wall = max_wall+1 if graph[x][y] == 1 else max_wall
                return dfs(back_nodes[-2], back_max_wall, count-1, back_nodes[:-1], True)

        for i in range(4):
            next = (x + dx[i], y + dy[i])
            X, Y = next

            if 0 <= X <= n-1 and 0 <= Y <= m-1 and not visited[X][Y]:
                if graph[X][Y] == 1:
                    if max_wall == 0:
                        continue
                    return dfs(next, max_wall-1, count+1, back_nodes)
                else:
                    return dfs(next, max_wall, count+1, back_nodes)

    result = dfs(start_node, max_wall, 1)
    print("result: ", result)

def main1():
    import sys
    input = sys.stdin.readline

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    n, m = map(int, input().split())
    #                   [wall?, visited -> 0:방문x, 1:방문, 2:벽부수고방문, 큐에 이미 몇 개 들어갔는지]
    graph = [list(map(lambda x:[int(x), 0, 0], input().strip())) for _ in range(n)]
                # (x, y, count, broke)
    start_node = (0, 0, 1, False)

    from collections import deque
    queue = deque([start_node])
    while queue:
        # print(queue)
        for q in range(len(queue)):
            x, y, count, broke = queue.popleft()
            graph[x][y][2] -= 1

            if x == n-1 and y == m-1:
                print(count)
                return

            # 벽 부수고 방문인지, 그냥 방문인지
            graph[x][y][1] = 2 if broke else 1 

            for i in range(4):
                X = x + dx[i]
                Y = y + dy[i]

                if 0 <= X <= n-1 and 0 <= Y <= m-1:
                    
                    # 이미 큐에 들어와 있는지 체크
                    if graph[X][Y][2] > 1: 
                        continue
                    
                    # 벽 부수지 않고 방문 
                    if graph[X][Y][0] == 0 and (graph[X][Y][1] == 0 or graph[X][Y][1] == 2):
                        if broke and graph[X][Y][1] == 2:
                            continue
                        queue.append((X, Y, count+1, broke))
                        graph[X][Y][2] += 1
                    
                    # 벽 부수고 방문
                    if not broke and graph[X][Y][0] == 1 and graph[X][Y][1] == 0:
                        queue.append((X, Y, count+1, True))
                        graph[X][Y][2] += 1

    if len(queue) == 0:
        print(-1)

        pass

def main():
    import sys
    import copy
    input = sys.stdin.readline

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    n, m = map(int, input().split())
    
    # 3차원 배열 만들 바에 그냥 배열 두 개로 나누자!! - 3차원 ㄹㅇ 이해불가야 ㅠㅠ
    graph = [list(map(int, input().strip())) for _ in range(n)] # 벽을 안 뚫고 가는 경로 표시할 그래프
    broke_graph = copy.deepcopy(graph) # 벽 뚫고 간 평행세계의 경로..표시할 그래프!

    from collections import deque
    start = (0, 0, 1, False)
    queue = deque([start])

    while queue:
        x, y, count, broke = queue.popleft()

        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]

            if x == n-1 and y == m-1:
                print(count)
                return

            if 0 <= next_x <= n-1 and 0 <= next_y <= m-1:
                if broke:
                    if broke_graph[next_x][next_y] == 0:
                        queue.append((next_x, next_y, count+1, True))
                        """
                        큐에 들여보낼 때 방문처리하기!!!!!!!!!!!!!!! 
                        큐에서 뺄 때 방문처리하면 중복된 노드들이 큐에 엄청 많이 들어감... 하 이것때문에 시간초과 메모리초과 그냥 난리부르스 ㅋㅋ..
                        """
                        broke_graph[next_x][next_y] = True
                else:
                    if graph[next_x][next_y] == 0: # 벽x
                        graph[next_x][next_y] = True
                        queue.append((next_x, next_y, count+1, False))
                    elif graph[next_x][next_y] == 1:
                        graph[next_x][next_y] == True
                        queue.append((next_x, next_y, count+1, True))

            
    if len(queue) == 0:
        print(-1)


main()