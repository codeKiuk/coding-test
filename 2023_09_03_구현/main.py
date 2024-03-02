# 이차원 행렬 상하좌우 문제 | 시작 지점 1,1
def solution1():
    directions_size = int(input())
    directions = list(map(str, input().split()))

    first_block = [1, 1]

    #   동, 서, 남, 북
    dx = [0, 0, 1, -1] # 행
    dy = [1, -1, 0, 0] # 열

    def check_overflow(block):
        # N * M 행렬을 벗어나게 되는 direction은 무시한다.
        if block[0] > directions_size or block[1] > directions_size or block[0] <= 0 or block[1] <= 0:
            return True
        else: 
            return False

    def move(direction):
        if direction == 'R':
            next_block = [first_block[0] + dx[0], first_block[1] + dy[0]]
            return first_block if check_overflow(next_block) else next_block
        elif direction == 'L':
            next_block = [first_block[0] + dx[1], first_block[1] + dy[1]]
            return first_block if check_overflow(next_block) else next_block
        elif direction == 'U':
            next_block = [first_block[0] + dx[3], first_block[1] + dy[3]]
            return first_block if check_overflow(next_block) else next_block
        elif direction == 'D':
            next_block = [first_block[0] + dx[2], first_block[1] + dy[2]]
            return first_block if check_overflow(next_block) else next_block
        
    for direction in directions:
        first_block = move(direction)

    print(first_block)

# 시각 문제
# 정수 N이 주어지면, 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램
def solution2():
    n = int(input())
    seconds = 60
    minutes = 60
    count = 0

    def loop():
        local_count = 0
        for i in range(minutes):
            minute = str(i)
            if minute.find('3') != -1:
                local_count += 60
            else:
                for j in range(seconds):
                    second = str(j)
                    if second.find('3') != -1:
                        local_count += 1
        return local_count

    for hour in range(n+1):
        string_hour = str(hour)
        if string_hour.find('3') != -1:
            count += 60 * 60
        else:
            count += loop()

    print(count)    
    pass

# 시각 문제
# 정수 N이 주어지면, 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램
# 간결한 버전
def solution3():
    h = int(input())

    count = 0
    for i in range(h+1): # 0시 ~ h시
        for j in range(60): # 0분 ~ 59분
            for k in range(60): # 0초 ~ 59초
                if '3' in str(i) + str(j) + str(k):
                    count += 1




