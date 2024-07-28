def main():
    import sys
    input = sys.stdin.readline

    N = int(input())

    # 기둥 a에서 b로 옮긴다 / 다른 나머지 하나의 기둥은 6-a-b
    # n번째 원판을 b로 옮기는 방법?
    # n-1번째 원판을 6-a-b로 옮긴다 recursion(a, 6-a-b, n-1)
    # n을 b로 옮기고, recursion(a, b, n)
    # n-1번째 원판을 b로 옮긴다 recursion(6-a-b, b, n-1)
    answer = 0
    stack = []
    def recursion(a, b, N):
        nonlocal answer
        answer += 1
        if N == 1:
            stack.append((a, b))
            return 1
        recursion(a, 6-a-b, N-1)
        stack.append((a, b))
        # print(f"{a} {b}")
        recursion(6-a-b, b, N-1)
    
    recursion(1, 3, N)

    print(answer)
    for a, b in stack:
        print(f"{a} {b}")

main()