def main():
    import sys
    input = sys.stdin.readline

    A, B, C = map(int, input().split())

    def recursion(A, B, C): 
        if B == 1:
            return A % C

        result = recursion(A, B//2, C) ** 2

        # B가 짝수인 경우
        if B % 2 == 0:
            return result % C
        # B가 홀수인 경우
        else:
            return result * A % C

    print(recursion(A, B, C))

main()