# 곱하기 혹은 더하기
# input : "02932136812305130357"
def solution1():
    user_input = input()

    index = 0   
    result = 0

    while True:
        if(index >= len(user_input)):
            break

        number = int(user_input[index])

        if number <= 1 or result <= 1:
            result += number
        else:
            result *= number
        
        index += 1

    print(result)



# 모험가 길드 
"""
첫째 줄에 모험가의 수 N이 주어진다. (1 <= N <= 100,000)
둘째 줄에 각 모험가의 공포도의 값을 N이하의 자연수로 주어지며, 각 자연수는 공백으로 구분한다.

여행을 떠날 수 있는 그룹 수의 최댓값을 출력한다.
"""
def solution2():

    from collections import Counter

    adventurers = int(input())
    fears = list(map(int, input().split()))
    fears.sort()
    
    group_count = 0
    result = 0

    for fear in fears:
        group_count += 1

        if (group_count >= fear):
            result += 1
            group_count = 0

    print(result)

solution2()