# 떡볶이 떡 만들기
# 파라메트릭 서치.. 최적화문제를 결정 문제로 바꾼다
# 적어도!!! m만큼의 떡을 가져간다.. m보다 크거나 같으면 되는거잖아?
# 탐색 범위가 너무 크면 (이 문제처럼 10억..) 이진탐색을 고려해보자
def solution1():
    from bisect import bisect_right
    n, m = map(int, input().split())

    # 떡의 개별 높이 정보
    array = list(map(int, input().split()))
    array.sort()

    start = 0 # start
    end = array[-1] # end

    answer = 0

    def binary_search(start, end, answer):
        print(f"start: {start}, end: {end} answer: {answer}")

        middle = (start + end) // 2

        if start >= end:
            return answer


        result = 0
        for i in range(n):
            if array[i] > middle:
                result += array[i] - middle
            

        if result == m:
            answer = middle
            return answer
        elif result > m:
            answer = middle
            # 중요 포인트
            # middle값은 위에서 사용했으니, 이진 탐색을 위해서 middle보다 크거나 작은 배열만 탐색해도 된다!!!!
            # 그냥 middle로 넘겨버리면 답 구할 수 없음
            return binary_search(middle+1, end, answer)
        else:
            return binary_search(start, middle-1, answer)
        pass


    print(binary_search(start, end, answer))

# 정렬된 배열에서 특정 수의 개수 구하기
def solution2():
    n, x = map(int, input().split())
    inputs = list(map(int, input().split()))

    from bisect import bisect_left, bisect_right

    smallest_index = bisect_left(inputs, x)
    biggest_index = bisect_right(inputs, x)

    result = biggest_index - smallest_index

    print("result: ", result)
    pass

solution2()