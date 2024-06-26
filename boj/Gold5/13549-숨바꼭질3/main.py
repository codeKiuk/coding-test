def main():
    import sys
    input = sys.stdin.readline

    n, k = map(int, input().split())

    max_input = 100000
    visited = [False] * (max_input+1)

    from collections import deque
    queue = deque([(n, 0)])
    result = 0
    while queue:
        popped = queue.popleft()
        visited[popped[0]] = True

        if visited[k]:
            target = [item[1] for item in queue if item[0] == k]
            sorted_target = sorted(target)
            result = sorted_target[0] if len(sorted_target) > 0 and sorted_target[0] < popped[1] else popped[1]
            break

        next_queue = [(popped[0]*2, popped[1]), (popped[0]+1, popped[1]+1), (popped[0]-1, popped[1]+1)]
        for i in next_queue:
            if 0 <= i[0] <= max_input and not visited[i[0]]:
                queue.append(i)
    print(result)      
        

main()


