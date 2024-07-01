from collections import deque

def bfs(graph, virus):
    vn, vm = virus
    queue = deque([virus])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]

            if 0 <= next_x < len(graph) and 0 <= next_y < len(graph[0]) and graph[next_x][next_y] == 0:
                graph[next_x][next_y] = 2
                queue.append((next_x, next_y))
    

def main():
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().split())

    virus_list = set([])
    blank_list = set([])
    graph = []

    for i in range(n):
        graph_list = list(map(int, input().split()))
        for j, k in enumerate(graph_list):
            if k == 2:
                virus_list.add((i, j))
            if k == 0:
                blank_list.add((i, j))

        graph.append(graph_list)

    from itertools import combinations
    from collections import Counter
    wall_combinations = list(combinations(blank_list, 3))
    max_result = 0

    import copy
    for wall_combination in wall_combinations:
        copied = copy.deepcopy(graph)
        x1, x2, x3 = wall_combination

        n1, m1 = x1
        n2, m2 = x2
        n3, m3 = x3

        copied[n1][m1] = 1
        copied[n2][m2] = 1
        copied[n3][m3] = 1

        for virus in virus_list:
            bfs(copied, virus)

        result = 0

        flattend = [item for sublist in copied for item in sublist]
        counter = Counter(flattend)
        result = counter[0]

        max_result = max(max_result, result)

    print(max_result)
    """
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
    """


main()