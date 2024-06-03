# 문제 1

# N : 10만.. 
# 파이썬.. 1초에 2천만
# nlogn 되지.. 10만log10만 = 50만 왜냐면 로그10만이 5니까
# 효율성도 맞을듯
def solution1():
    from bisect import bisect_left, bisect_right

    A = [3, 1, 4,1,5]

    # 정확한 개수가.. 나와야 한다..
    # 일단 Sort를 갈긴다..  -> nlogn..
    A.sort()

    # bisect left , bisect right -> 해서 Index 찾는다.. 개수 찾는다..
    # 근데 이게.. N이..EXACTly X times 나타나야 한다 일단 조건이.. -> 최대 10만 길이니까 X는 최대 10만이겠찌?

    # 큰 수부터 작은 수까지 loop 돈다
    i = 100000

    while i > 0:
        smallest_index = bisect_left(A, i)
        biggest_index = bisect_right(A, i)

        print(f"i: {i} biggest: {biggest_index}, smallest: {smallest_index}")

        result = biggest_index - smallest_index

        if result == i:
            print(i)
            return i
        i -= 1
    
    return 0
    

# solution1()

# 개구리는 현재 위치에서 크거나 같은 옆 인덱스로 이동이 가능하다 (양쪽 다..)
# 두 개구리가 가장 멀어질 수 있는 거리는..?? 이때 거리는 J - K + 1 (J는 인덱스, K도 인덱스)
# 답은 맞았는데 효율성이 틀릴 듯
# 근데 음.. 제출 후에 시발 sol2가 빈칸으로 리로드되던데.. 시스템 오류인가.. 제출 잘 된 거 맞겠지..??ㅜㅜㅜㅜㅜㅜ
def solution2():
    # array length: 20만.. 20만log20만 = 100만 nlogn 까지 가능
    # 두 개구리가 서로 멀어질 수 있는.. 최적의 블록을 찾는다

    # 특정 index에서 양쪽으로 얼마나 멀리 갈 수 있느냐
    # 현재 index의 원소값이랑 같거나 큰 값으로만 이동가능.. 무조건 인접 인덱스로만 가능

    # 일단 작은 원소값을 찾아야 하지 않니? 

    # 최적의 블록은.. 양옆으로 sorting이 좀 되어있어야 한다
    # 최적 블록 기준 왼쪽은 내림차순으로 오고, 오른쪽으로 오름차순으로 가면 된다
    # 최종 거리는.. 왼쪽 내림차순 개수 + 오른쪽 오름차순 개수 + 1
    # ex. [ 10, 9, 8, 7...4,최적=3, 4, 5 , 6 , 7 ,8 ...]

    # DP구나.. 이전 결과값 저장해놓으면 되겠따..

    blocks = [2,6,8,6]

    def get_right(array, start):
        target = start
        for idx, val in enumerate(array):
            if idx == len(array) - 1:
                target = idx + start
            elif val <= array[idx+1]:
                target = idx+1 + start
            elif val > array[idx+1]:
                break
        return target

    def get_left(array, start):
        target = start
        
        print(f"array: {array}")

        start_index = len(array) - 1

        while start_index > -1:
            curr = array[start_index]
            next_val = array[start_index-1]

            if curr > next_val:
                break
            elif curr <= next_val:
                target = start - start_index
            start_index -= 1
        return target
        return target
            

    distance = 0
    for index, value in enumerate(blocks):
        if index == 0:
            # 오른쪽 오름차순 개수만 세기
            right_index = get_right(blocks, 0)
            print(f"right_index in INDEX == 0: {right_index}")
            if distance < right_index + 1:
                distance = right_index + 1
        elif index == len(blocks) -1:
            # 왼쪽 내림차순 개수만 세기
            left_index = get_left(blocks, index)
            print(f"left_index in INDEX == LAST: {left_index}")
            if distance < left_index:
                distance = left_index
        else:
            # 왼쪽 내림차순 개수 + 오른쪽 오름차순 개수세기
            left_index = get_left(blocks[:index+1], index)
            right_index = get_right(blocks[index:], index)
            print(f"left_index: {left_index}, right_index: {right_index}")
            if distance < left_index - right_index:
                distance = left_index - right_index
    print(distance)
    return distance
    pass

# solution2()

# 테케도 하나 틀려가지고.... 답도 틀릴 듯 효율성은 당연히 틀리구 ㅜㅜ 
def solution3():
    import math

    A = [2,1,3]
    S = 2 # 정수


    # A의 배열조각의 산술평균이 S가 되는 경우의 수
    #  ex. A = [2, 1, 3] => [2], [2,1,3] , [1,3] => 3가지

    # N 10만
    # 어쨌든.. 배열조각이 연속적이어야 한다..

    dp = [
         # 1개짜리 배열조각 합들
         # 2개짜리 배열조각 합들
         # 3개짜리 배열조각 합들 ...
        # ...
    ]

    max_length = len(A)

    dp = [[0] * len(A) for _ in range(max_length+1)]

    for i in range(1, max_length+1):
        for j, val in enumerate(A):
            if i == 1:
                dp[i][j] = val
            else:
                if j + i >= len(A) + 1:
                    break
                dp[i][j] = sum(A[j:j+i])

    print(dp)

    result = 0
    for i, arr in enumerate(dp):
        if i == 0:
            continue
        for j, val in enumerate(arr):
            print(f"val, i: {val} {i} {int(val/2)}")
            if j >= math.ceil(len(A) // i):
                break
            if int(val / i) == S:
                result += 1
        


    if result > 1000000000:
        return 1000000000

    print(result)
    return result
    pass

# solution3()

def main():

    array = [4,5,1,3,2,]

    i = len(array) - 1

    while i >= 0:
        j = len(array) - 1

        while j >= 1:
            if array[j] < array[j-1]:
                t = array[j]
                array[j] = array[j-1]
                array[j-1] = t
            print(array)
            j -= 1
        i -= 1

    

main()