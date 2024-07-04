def main():
    import sys
    input = sys.stdin.readline

    N, M = map(int, input().split())

    set_list = []

    for _ in range(N):
        string = input()
        set_list.append(string)
    
    S = set(set_list)

    count = 0
    for _ in range(M):
        string = input()
        if string in S:
            count += 1

    print(count)

main()
