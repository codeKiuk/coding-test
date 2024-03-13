# 떡볶이 떡 만들기
# 파라메트릭 서치.. 최적화문제를 결정 문제로 바꾼다
# 적어도!!! m만큼의 떡을 가져간다.. m보다 크거나 같으면 되는거잖아?
def solution1():
    from bisect import bisect_right
    n, m = map(int, input().split())

    # 떡의 개별 높이 정보
    array = list(map(int, input().split()))
    array.sort() # 오름차순

    # 4 6cm
    # 0 1 2 3


    answer = 0

    def binary_search(array, start, end):
        if start >= end:
            return None

        middle = (start + end)//2
        middle_value = array[middle]

        left_side = array[:middle]
        right_side = array[middle:]

        result = 0

        for i in right_side:
            result += i - middle_value

        if result == m:
            return middle_value
        elif result > m:
            return binary_search(array, middle+1, end)
        else:
            return binary_search(array, start, middle-1)

    print(binary_search(array, 0, n-1))
    pass

solution1()