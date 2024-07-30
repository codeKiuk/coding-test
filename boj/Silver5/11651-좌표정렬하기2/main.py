import sys
def main():
    input = sys.stdin.readline
    N = int(input())

    pointers = [list(map(int, input().split())) for _ in range(N)]
    
    sorted_pointers = sorted(pointers, key=lambda x : (x[1], x[0]))

    for pointer in sorted_pointers:
        x, y = pointer
        print(f"{x} {y}")



main()