def main():

    import sys
    input = sys.stdin.readline

    N, P = map(int, input().split())

    from collections import deque

    input_list = deque([])
    for i in range(N):
        n, p = map(int, input().split())
        input_list.appendleft((n, p))
    
    
    queue = deque(input_list)
    stack = [deque([]) for _ in range(N)]
    

    # 누르거나 떼는 게 한 번 카운트
    count = 0
    while queue:
        n, p = queue.pop()
        target_stack = stack[n-1]

        if len(target_stack) == 0:
            target_stack.append(p)
            count += 1

        elif target_stack[-1] == p:
            continue

        elif target_stack[-1] > p:
            while target_stack and target_stack[-1] > p:
                target_stack.pop()
                count += 1

            if len(target_stack) == 0:
                target_stack.append(p)
                count += 1
            elif target_stack[-1] == p:
                continue
            else:
                target_stack.append(p)
                count += 1

        else:
            target_stack.append(p)
            count += 1

    print(count)

main()
        
"""        
3 15
1 5
1 10
1 5
"""
