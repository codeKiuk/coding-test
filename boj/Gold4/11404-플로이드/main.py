import sys
def main():
    input = sys.stdin.readline
    N = int(input())
    M = int(input())
    # 한 도시에서 다른 도시로 가는 최단경로의 최대값은 99 곱하기 100000 이다. 
    # -> a에서 b로 갈때 99개의 도시를 거쳐가야 하고, 그 99개의 경로가 최대 100000 이기 때문..
    # 최대값 설정 잘 못 하면 틀릴 수도.. 이거 참 어렵넹...
    d = [[10000000000] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        start, end, cost = map(int, input().split())
        d[start][end] = min(d[start][end],cost)

    for i in range(1, N+1):
        for j in range(1, N+1):
            if j == i:
                continue
            for k in range(1, N+1):
                # i를 거쳐가는 경우, j->k
                if k == i:
                    continue
                if j != k:
                    d[j][k] = min(d[j][k], d[j][i] + d[i][k])
                    d[k][j] = min(d[k][j], d[k][i] + d[i][j])
                else:
                    d[j][k] = 0


    for i in range(1, N+1):
        for j in range(1, N+1):
            print(d[i][j] if d[i][j] != 10000000000 else 0, end=" ")
        print()
main()