import sys
def main():
    input = sys.stdin.readline

    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    B = list(map(int, input().split()))

    sorted_a = sorted(A)

    def binary_search(number, sorted_list, left, right):
        if left > right:
            return False

        mid = (left + right) // 2
        mid_val = sorted_list[mid]

        if number == mid_val:
            return True
        elif number > mid_val:
            return binary_search(number, sorted_list, mid+1, right)
        else:
            return binary_search(number, sorted_list, left, mid-1)



    for b in B:
        is_in_a = binary_search(b, sorted_a, 0, N-1)
        if is_in_a:
            print(1)        
        else:
            print(0)

main()