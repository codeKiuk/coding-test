def main():
    import sys
    input = sys.stdin.readline

    n, k = map(int, input().split())

    from collections import deque

    queue = deque([n])
    count = 0
    max_input = 100000
    visited = [False] * (max_input + 1)
    
    while queue:
        if k in queue:
            break
        for _ in range(len(queue)):
            popped = queue.popleft()
            next_queue = [popped + 1, popped - 1, popped * 2]
            for next_pos in next_queue:
                if 0 <= next_pos <= max_input and not visited[next_pos]:
                    visited[next_pos] = True
                    queue.append(next_pos)
        count += 1

    print(count)


main()