def main():
    import math, heapq, sys
    input = sys.stdin.readline


    test_cases = int(input())

    for test_case in range(test_cases):
        size = int(input())
        input_list = []

        if size > 10:
            line_count = math.ceil(size / 10)

            for _ in range(line_count):
                input_list += list(map(int, input().split()))

        else:
            input_list = list(map(int, input().split()))

        output_count = math.ceil(size/2)
        result_list = []
        
        # 중앙값 구하기
        # 정렬로는 안 된다..-> heap?
        # 힙 만들고, 3번째 홀수면 -> 2번 heappop 시키면 중앙값 나옴
        for i, value in enumerate(input_list):
            modulo = i % 2
            dividend = i / 2
            if i % 2 == 0: # 이때가 홀수번째 
                # 전체말고 부분 리스트 만들어서 heapify
                target_list = input_list[:i+1]
                heapq.heapify(target_list)

                # dividnend 수만큼 heappop하면된다
                for _ in range(int(dividend)):
                    heapq.heappop(target_list)
                result_list.append(target_list[0])
            else:
                continue

        print(output_count)
        if len(result_list) > 10:
            result_size = math.ceil(len(result_list) / 10)
            for _ in range(result_size):
                print(f"{' '.join(list(map(str, result_list[:10])))}")
                result_list = result_list[10:]
        else:
            print(f"{' '.join(list(map(str, result_list)))}")
        

main()