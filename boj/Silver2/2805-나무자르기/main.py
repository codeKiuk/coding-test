import sys
def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    trees = list(map(int, input().split()))
    
    def get_height(tool_height):
        nonlocal trees
        height = 0
        for tree in trees:
            if tool_height < tree:
                height += tree - tool_height

        return height

    start = 1
    end = max(trees)

    while start <= end:
        mid = (start + end) // 2
        height = get_height(mid)

        if height >= M:
            start = mid + 1
        else:
            end = mid - 1

        

    print(end)

main()

"""
2 10
5 5

ans 0
"""