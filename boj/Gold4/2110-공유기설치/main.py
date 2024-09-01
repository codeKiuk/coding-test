import sys
def main():
    input = sys.stdin.readline

    N, C = map(int, input().split())
    location_list = sorted([int(input()) for _ in range(N)])

    # 거리에 대해 이분탐색으로 parametric search 돌린다..
    # 두 접점 사이의 거리가 최소 1, 최대 location_list[-1] - location_list[0]..
    start = 1
    end = location_list[-1] - location_list[0]  

    answer = float('inf')
    while start <= end:
        mid = (start + end) // 2
        count = 1 # 처음 집에는 무조건 공유기 설치

        prev_house = location_list[0]
        for i in range(1, N):
            next_house = location_list[i]

            if next_house - prev_house >= mid:
                count += 1
                prev_house = next_house

        if count >= C:
            answer = mid
            start = mid + 1
            continue

        end = mid - 1



    print(answer)

main()

"""
1 2 4 8 9


10 4
1
2
3
4
5
6
7
8
9
10

3
===
5 4
1
3
5
10
11

2

"""