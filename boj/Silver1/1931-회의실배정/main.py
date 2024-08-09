import sys
def main():
    input = sys.stdin.readline

    N = int(input())
    meeting_list = [list(map(int, input().split())) for _ in range(N)]
    sorted_meeting = sorted(meeting_list, key=(lambda x: (x[1], x[0])))
    count = 1
    
    start_time = sorted_meeting[0][0]
    end_time = sorted_meeting[0][1]

    for meeting in sorted_meeting[1:]:
        next_start_time = meeting[0]
        next_end_time = meeting[1]
        if next_start_time >= end_time:
            count += 1
            start_time = next_start_time
            end_time = next_end_time

    print(count)

main()
