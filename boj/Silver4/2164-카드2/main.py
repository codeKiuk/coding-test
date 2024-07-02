def main():
    import sys
    input = sys.stdin.readline

    from collections import deque

    n = int(input())
    queue = deque([i+1 for i in range(n)])

    while queue:
        if len(queue) == 1:
            break
        queue.popleft()
        queue.rotate(-1)

    print(queue[0])

main()