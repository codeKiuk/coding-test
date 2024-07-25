"""
0 0 1 0
1 0 0 0
0 0 0 1
0 1 0 0

한 라인에 하나의 퀸밖에 오지 못 한다. 모든 경우에서
가로 세로 대각선
순열 느낌?

(1, 3) (2, 1) (3, 2)
0 0 1
1 0 0
0 1 0
"""

def main():
    import sys
    from copy import deepcopy
    from itertools import product
    from collections import deque, Counter

    input = sys.stdin.readline
    N = int(input())
    permutation = list(product(range(1, N+1), range(1, N+1)))
    permutation_count = Counter(permutation)
    permutation_keys = permutation_count.keys()
    answer = 0

    def recursion(nodes):
        nonlocal answer

        valid_nodes = []
        max_x = max(node[0] for node in nodes)
        
        if max_x == N:
            answer += 1
            return

        for y in range(1, N+1):
            is_valid = True
            for node in nodes:
                node_x, node_y = node

                if y == node_y or abs(max_x+1 - node_x) == abs(y - node_y):
                    is_valid = False
                    break
            
            if is_valid:
                valid_nodes.append((max_x+1, y))
            
        for valid_node in valid_nodes:
            valid_x, valid_y = valid_node
            nodes.append(valid_node)
            recursion(nodes)
            nodes.pop()
                
                

    queue = deque([])

    for i in permutation_keys:
        x, y = i

        if x > 1:
            break

        if x == 1:
            queue.append([i])
            recursion([i])
            queue.pop()

    print(answer)

main()