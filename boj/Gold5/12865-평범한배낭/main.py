import sys
from bisect import bisect_left
from collections import deque

def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    # (무게, 가치)
    array = [list(map(int, input().split())) for _ in range(N)]
    
    dp = [[0]*(K+1) for _ in range(N+1)]

    if N == 1:
        print(array[0][1] if array[0][0] <= N else 0)
        return

    for i in range(1, N+1):
        # i번째에서 허용할 무게 j
        for j in range(K+1):
            n, k = array[i-1]

            if n <= j: # 이번 루프 아이템 넣을 수 있는 경우
                # 이번 루프 아이템만큼의 무게 빼고 이번 루프 아이템을 넣는다 VS 이번 루프 아이템 넣지 않는다
                dp[i][j] = max(dp[i-1][j-n] + k, dp[i-1][j])
            else: # 이번 루프 아이템 넣을 수 없는 경우
                dp[i][j] = dp[i-1][j]
    
    print(max(dp[N]))

main()



def main2():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    # (무게, 가치)
    array = [list(map(int, input().split())) for _ in range(N)]
    
    #   [몇번째까지 봤냐, 총 무게] = 가치 / dp[1][6] = 첫번째꺼 넣었을 때 가치, dp[1][0] = 0 => 이 가치를 최대로 만들기
    # result = max(dp[N])
    dp = [[0]*(K+1) for _ in range(N+1)]
    dp[1][0] = 0
    dp[1][array[0][0]] = array[0][1]
    accumulated_weights = deque([array[0][0]])

    if N == 1:
        print(array[0][1])
        return
    
    for i in range(2, N+1):
        for j in range(len(accumulated_weights)):
            accumulated_weight = accumulated_weights.popleft()
            left_weight = K - accumulated_weight
            current_item_weight = array[i-1][0] # 이번 루프 아이템의 무게
            
            if current_item_weight > left_weight: # 이번 루프 아이템 넣지 못 하는 경우
                # 이번 루프 아이템을 넣지 않는다
                dp[i][accumulated_weight] = dp[i-1][accumulated_weight]
                accumulated_weights.append(accumulated_weight)

                # 저번 루프 아이템을 빼고 이번 루프 아이템을 넣는다 (가능하면..)
                next_weight = accumulated_weight - array[i-2][0] + current_item_weight
                if next_weight <= K and next_weight >= 0:
                    dp[i][next_weight] = dp[i-1][accumulated_weight] - array[i-2][1] + array[i-1][1] 
                    accumulated_weights.append(next_weight)
            else: # 이번 루프 아이템을 넣을 수 있는 경우 무조건 넣는다
                next_weight = accumulated_weight + current_item_weight
                dp[i][next_weight] = dp[i-1][accumulated_weight] + array[i-1][1]
                accumulated_weights.append(next_weight)
    

    print(max(dp[N]))