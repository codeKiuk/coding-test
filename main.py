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
        if block[0] >= directions_size or block[1] >= directions_size or block[0] <= 0 or block[1] <= 0:
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

solution1()

