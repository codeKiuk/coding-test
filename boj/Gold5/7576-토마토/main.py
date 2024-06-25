def main():
    # INITIALIZATION START
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().split())
    boxes = []
    all_boxes = n*m
    empty_boxes = 0
    starting_box_place = []

    for i in range(m):
        column_boxes = list(map(int, input().split()))
        boxes.append(column_boxes)

        for j in range(n):
            if column_boxes[j] == -1:
                empty_boxes += 1
            elif column_boxes[j] == 1:
                starting_box_place.append((i, j))

    # check if all tomatoes can go rotten
    target_tomatoes = all_boxes - empty_boxes
    
    # INITIALIZATION DONE

    date_count = 0
    from collections import deque
    queue = deque(starting_box_place)
    
    # 좌 우 하 상
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        # 큐 한 번에 다 정리하고 날짜 카운드
        # 스타팅 포인트 전부 하루에 한 번씩 돌려야 함
        for _ in range(len(queue)):
            popped = queue.popleft()
            target_tomatoes -= 1
            x, y = popped
            for i in range(4):
                X = x + dx[i]
                Y = y + dy[i]

                if X >= 0 and Y >= 0 and X < m and Y < n and boxes[X][Y] == 0:
                    queue.append((X, Y))
                    boxes[X][Y] = 1
        date_count += 1

    if target_tomatoes > 0:
        print("-1")
        return
    print(date_count-1)

main()