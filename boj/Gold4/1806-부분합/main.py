import sys
def main():
    input = sys.stdin.readline

    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    min_length = float('inf')
    start_idx = 0
    end_idx = 1

    if A[start_idx] >= M:
        print(1)
        return

    total = A[start_idx] + A[end_idx]
    while start_idx < N and end_idx < N:
        if total >= M:
            min_length = min(min_length, end_idx - start_idx + 1)
            total -= A[start_idx] if start_idx < N else 0
            start_idx += 1
        else:
            end_idx += 1
            total += A[end_idx] if end_idx < N else 0


    print(min_length if min_length != float('inf') else 0)    

main()


