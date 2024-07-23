from collections import Counter

def main():
    import sys
    input = sys.stdin.readline

    N, M, B = map(int, input().split())

    graph = [list(map(int, input().split())) for _ in range(N)]
    
    height_counter = Counter(block for row in graph for block in row)
    min_height = min(height_counter.keys())
    max_height = max(height_counter.keys())

    min_time = float('inf')
    answer_height = -1
    for target_height in range(min_height, max_height+1):
        removed_blocks = 0
        added_blocks = 0
        for height, count in height_counter.items():
            gap = height - target_height
            if gap > 0:
                removed_blocks += gap * count
            elif gap < 0:
                added_blocks += -gap * count

        time = 2*removed_blocks + added_blocks
        left_blocks = B + removed_blocks - added_blocks
        if left_blocks < 0:
            continue
        if time <= min_time:
            min_time = time
            answer_height = target_height

    print(f"{min_time} {answer_height}")


main()


"""
1 7 10
65 64 64 64 63 62 0

148 56
"""