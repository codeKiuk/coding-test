def main():
    import sys
    from collections import deque
    input = sys.stdin.readline

    test_case = int(input())

    result_list = []

    for idx in range(test_case):
        func = list(input().strip())
        size = int(input())
        error = False
        is_reverse = False

        if size == 0:
            input()
            array = deque([])
        else:
            array = deque(list(map(int, input().strip('\n').strip('[').strip(']').split(','))))
            

        for p in func:
            if p == 'D':
                
                if len(array) == 0:
                    error = True
                    break
                
                if is_reverse:
                    array.pop()
                else:
                    array.popleft()
            
            if p == 'R':
                is_reverse = not is_reverse
        
        if error:
            # print('error')
            result_list.append('error')
        else:
            if is_reverse:
                result_list.append(f"[{','.join(map(str, reversed(array)))}]")
            else:
                result_list.append(f"[{','.join(map(str, array))}]")

    for result in result_list:
        print(result)

main()

"""
4
RDD
4
[1,2,3,4]
DD
1
[42]
RRD
6
[1,1,2,3,5,8]
D
0
[]


3
RDD
4
[1,2,3,4]
DD
1
[42]
RRD
6
[1,1,2,3,5,8]

2
RDD
4
[1,2,3,4]
RRD
6
[1,1,2,3,5,8]
"""