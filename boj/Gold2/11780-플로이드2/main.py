import sys
def main():
    input = sys.stdin.readline
    N = int(input())
    M = int(input())
    d = [[100000 * 99] * (N+1) for _ in range(N+1)]
    history = [[0] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        start, end, cost = map(int, input().split())
        d[start][end] = min(d[start][end], cost)
        history[start][end] = end

    for mid in range(1, N+1):
        for u in range(1, N+1):
            if u == mid:
                continue
            for v in range(1, N+1):
                if v == mid:
                    continue
                if u != v:
                    if d[u][mid] + d[mid][v] < d[u][v]:
                        d[u][v] = d[u][mid] + d[mid][v]
                        history[u][v] = history[u][mid]
                else:
                    d[u][v] = 0

    for i in range(1, N+1):
        for j in range(1, N+1):
            print(f"{d[i][j] if d[i][j] != 100000 * 99 else 0}", end=" ")
        print()

    for i in range(1, N+1):
        for j in range(1, N+1):
            if i == j or history[i][j] == 0:
                print(0)
                continue
            path = [i]
            end = history[i][j]
            while end != j:
                path.append(end)
                end = history[end][j]
            path.append(j)
            print(len(path), end = " ")
            print(*path)


main()