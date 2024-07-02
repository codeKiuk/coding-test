def main():
    import sys
    input = sys.stdin.readline

    n = int(input())

    from collections import deque
    stack = deque([])

    for _ in range(n):
        k = int(input())
        if k == 0:
            stack.pop()
        else:
            stack.append(k)

    result = sum(stack)

    print(result)
            

main()