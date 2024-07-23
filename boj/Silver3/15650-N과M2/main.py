def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    N, M = map(int, input().split())

    permutation = deque([])

    def nm(permutation):
        # size가 이미 M인 경우
        # 순열에 이미 들어가 있는 경우

        if len(permutation) == M:
            print(' '.join(map(str, permutation)))
            return
            
        for i in range(1, N+1):

            if len(permutation) > 0 and i < permutation[-1]:
                continue

            if i in permutation:
                continue


            permutation.append(i)
            nm(permutation)
            permutation.pop()

    nm(permutation)

main()