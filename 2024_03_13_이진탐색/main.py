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

        if start >= end:
            return answer


        result = 0
        for i in range(n):
            if array[i] > start:
                result += array[i] - start
            

        middle = (start + end) // 2
        if result == m:
            answer = start
            return answer
        elif result > m:
            answer = start
            return binary_search(middle+1, end, answer)
        else:
            return binary_search(start, middle, answer)
        pass


    print(binary_search(start, end, answer))

solution1()