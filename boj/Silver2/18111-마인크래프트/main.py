def main():
    import sys
    sys.setrecursionlimit(10**6)
    input = sys.stdin.readline

    N, M, B = map(int, input().split())

    global graph
    graph = []
    min_height = 0
    max_height = 0

    for _ in range(N):
        graph_line = list(map(int, input().split()))
        graph.append(graph_line)

        min_height = min(min_height, min(graph_line))
        max_height = max(max_height, max(graph_line))

    # 250,000 * 256..
    def recursion(node, blocks, target_height, current_time=0):
        x, y = node
        height = graph[x][y]

        if height == target_height:
            pass
        elif height > target_height:
            gap = height - target_height
            current_time += gap * 2
        else:
            gap = target_height - height
            if gap > blocks:
                return 500 * 500 * 256
            else:
                current_time += gap
                blocks -= gap
            

        if x == N-1 and y == M-1:
            return current_time
        elif y == M-1:
            return recursion((x+1, 0), blocks, target_height, current_time)
        else:
            return recursion((x, y+1), blocks, target_height, current_time)

    min_time = 500 * 500 * 256
    target_height = 0
    for i in range(min_height, max_height+1):
        possible_min = recursion((0,0), B, target_height=i)
        if min_time >= possible_min:
            min_time = possible_min
            target_height = i

    print(f"{min_time} {target_height}")


main()