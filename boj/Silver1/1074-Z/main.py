def main():
    import sys
    input = sys.stdin.readline

    N, R, C = map(int, input().split())

    """
    N이 1일 때 2*2 로 네칸 -> Base Case 1개 2**0 4분면 1개
    N이 2일 때 4*4 로 16칸.. base case가 4개 2**2 4분면 4개
    N이 3일 때 base case가 16개 2**4 4분면 16개

    0| 0 1 0 0
    1| 2 3 0 0
    2| 0 0 0 T (2,3)->(0,1)
    3| 0 0 0 0
    (0, 0) : 1
    (0, 1) : 2
    (1, 0) : 3
    (1, 1) : 4
    """

    def recursion(N, R, C, base_count=0):
        criterion = (2**N)//2

        if N == 1:
            if R >= criterion and C >= criterion: # 4분면
                return base_count + 3
            elif R >= criterion and C < criterion: # 3분면
                return base_count + 2
            elif R < criterion and C >= criterion: # 2분면
                return base_count + 1
            else: # 1분면
                return base_count

        # 몇 사분면에 속하냐..
        if R >= criterion and C >= criterion: # 4분면
            return recursion(N-1, R-criterion, C-criterion, base_count + (2**(N-1))**2 * 3)
        elif R >= criterion and C < criterion: # 3분면
            return recursion(N-1, R-criterion, C, base_count + (2**(N-1))**2 * 2)
        elif R < criterion and C >= criterion: # 2분면
            return recursion(N-1, R, C-criterion, base_count + (2**(N-1))**2)
        else: # 1분면
            return recursion(N-1, R, C, base_count)

    answer = recursion(N, R, C)
    print(answer)

main()