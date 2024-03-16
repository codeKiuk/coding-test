# 다이나믹 프로그래밍
# 개미 전사 문제
def solution1():
    # 인접한 식량창고를 털지 않도록 하는 최대 식량 얻기

    n = int(input())
    array = list(map(int, input().split()))


    # solution BOTTOM UP
    d = [0] * n
    d[0]  = array[0]
    d[1] = max(array[1],array[0])

    for i in range(2, n):
        d[i] = max(d[i-1], d[i-2] + array[i])

    print(d[n-1])

# 1로 만들기
# 주어진 값을 1로 만들고자 할 때, 연산 사용의 최솟값을 구해라
def solution2():
    n = int(input())

    # 5로 나누어 떨어지면 5로 나눈다
    # 3으로 나누어 떨어지면 3으로 나눈다
    # 2로 나누어 떨어지면 2로 나눈다
    # 1을 뺀다

    # 목표값은 1이다.

    #  5로 나누어떨어지는게 가장빠르잖아 -> 34야 만약에?
    # 34 -> 4번빼 -> 5로나눠 == 6 -> 1빼 == 5 -> 5로나눠 == 1 : 7번
    # 34 -> 17 -> 16 -> 8 -> 4 -> 2 -> 1
    # 34 -> 33 -> 11 -> 10 -> 2 -> 1 : 5
    # 1뺏을 때 5,3,2의 배수가 되면 5,3,2로 나누는게 더 빠르다
    # 그리디는 안 되네..=

    i = n
    count = 0

    while True:
        if i == 1:
            break
        
        count += 1

        if i % 5 == 0:
            i = i // 5
            continue
        elif (i-1) % 5 == 0:
            i -= 1
            continue
        elif i % 3 == 0:
            i = i // 3
            continue
        elif (i-1) % 3 == 0:
            i -= 1
            continue
        elif i % 2 == 0:
            i = i // 2
            continue
        elif (i-1) % 2 == 0:
            i -= 1
            continue


    # BOTTOM UP 방식 솔루션

    d = [0] * (n+1)

    for i in range(2, n + 1):
        # +1하는 이유는.. 횟수 카운팅해야해서

        if i % 2 == 0:
            d[i] = min(d[i-1] + 1, d[i//2] + 1)
        if i % 3 == 0:
            d[i] = min(d[i-1] + 1, d[i//3] + 1)
        if i % 5 == 0:
            d[i] = min(d[i-1] + 1, d[i//5] + 1)

    print(d[n])
    pass


# 효율적인 화폐 문제
# N가지 종류 화폐 존재 / 최소한으로 개수를 이용해서 합이 M이 되도록 한다
# N가지 화폐로 M원을 만들 수 없다면 -1
def solution3():
    n, m = map(int, input().split())
    moneys = []
    for i in range(n):
        moneys.append(int(input()))

    
    #  moneys에 m의 약수가 없으면 -1
    # 혹은 moneys의 원소들로 m의 약수 중 하나라도 만들 수 없으면 -1
    # 일단 M의 약수를 구해라
    division_m = [x for x in range(1, m+1) if m % x == 0]


    dp = [0] * len(division_m)
    #  dp[len(division_m)-1] = 1 무조건 1인거지..
    # dp[len(division_m)-2] = // 몫만큼.. 곱해준다

    import math
    count = math.inf

    from itertools import combinations


    divisible = False
    # 루프 돌면서 맥스 count 구하기..
    for index, i in enumerate(division_m):
        #  i는 m의 약수
        # moneys에서 i 그 자체거나, i를 만들 수 있는 조합을 찾아라..

        if i in moneys:
            divisible = True
            dp[index] = dp[index] if dp[index] != 0 else m // i
            count = min(count, dp[index])
        # moneys의 원소들의 조합으로 m의 약수를 만들 수 있는지 확인
        else:
            if dp[index] != 0:
                count = min(count, dp[index])
            elif n >= 3:
                for num in range(2, n):
                    comb = list(combinations(moneys, num))
                    for combination in comb:
                        if sum(combination) == i:
                            divisible = True
                            dp[index] = len(combination) * (m // i)
                            count = min(count, dp[index])
                            break
            else:
                comb = list(combinations(moneys, n))
                for combination in comb:
                    if sum(combination) == i:
                        divisible = True
                        dp[index] = len(combination) * (m // i)
                        count = min(count, dp[index])
                        break

    print(f"{count if divisible else -1}")



    ### 실제 DP 풀이..

    d = [10001] * (m+1) # 10001은 불가능한 수로 초기화
    d[0] = 0

    # 내가 가지고 있는 화폐 n을 이용해서..
    # m을 순회하면서.. 만들 수 있는지 확인한다
    # Ai = min(Ai, Ai-k + 1) k는 화폐의 단위

    for i in range(n):
        for j in range(0, m+1):
            # i-k원을 만들 수 있는지 확인하기
            if d[j - moneys[i]] != 10001:
                d[j] = min(d[j], d[j - moneys[i]] + 1) # 1은 화폐의 개수, 이번 i원 한 개 추가하는 거니까
    
    print(d[m] if d[m] != 10001 else -1)
    pass

# 금광 문제
# 오른쪽, 오른쪽 아래, 오른쪽 위 3가지 방향으로만 이동 가능
# 최대 얼마의 금을 캘 수 있는지
def solution4():
    T = int(input()) # 테스트 케이스 개수 -> 총 몇 번 루프 돌리냐
    for _ in range(T):
        N, M = map(int, input().split())
        array = list(map(int, input().split()))

        graph = [
            # [M개]
        ]

        print(f"array: {array}")
        for i in range(0, len(array), M):
            graph.append(array[i:i+M])

        print(graph)

        
        # max(a0.1, a1.2) 27 vs 32
        # 1 6 1 0 11 0       
        # 2 2 7 1 0 0
        # 5 0 2 3 0 0
        # 0 6 1 2 5 9


        # 일단 현재 열에서 최대값을 선택한다
        # 한 열(column - M)이 추가됐을 때, 
        # 지금까지 얻었던 금광개수보다 더 많은 금광을 얻을 수 있는 애(x)가 나타난다면
        # 현재 선택한 행열에서 도달할 수 있다면 그냥 가면 되고.. 도달 불가면 x에 도달할 수 있는 경로로 업데이트

        # 아냐.. 그냥 graph 값을 업데이트하면 되잖아 최댓값으로??
        dx = [-1, -1, -1]
        #    왼쪽위, 왼쪽, 왼쪽아래
        dy = [1, 0, -1]

        for i in range(0, M): # 열
            for j in range(0, N): # 행
                curr = graph[j][i]
                if i == 0: # 첫 열이면 그대로 두기
                    continue
                if j == 0: # 첫 행이면 2개 중 최대값
                    graph[j][i] = max(curr + graph[j][i-1], curr + graph[j+1][i-1])
                    continue
                if j == N-1: # 마지막 행이면 2개 중 최대값
                    graph[j][i] = max(curr + graph[j][i-1], curr + graph[j-1][i-1])
                    continue
                graph[j][i] = max(curr + graph[j][i-1], curr + graph[j-1][i-1], curr + graph[j+1][i-1])

        max_value = 0
        for i in range(0, N):
            max_value = max(max_value, graph[i][M-1])
        print(max_value)


    pass

# 병사 열외시키기 문제
# 전투력은 최대로 만들면서..
def solution5():
    N = int(input())
    inputs = list(map(int, input().split()))

    # 15 11 4 8 5 2 4
    # -> 중간에 낀 4랑 2 열외시키면
    # 전투력 최대인 내림차순이 된다

    # 50 33 31 29 13 39 3 4 4 4 1

    # 열외시키고 다음 애들로 열외한 애 이길거냐, 열외 시키지 않고 가져갈거냐..

    drop_count = 0

    for i, curr in enumerate(inputs):
        if i == N-1:
            break
        next = inputs[i+1]

        if curr > next:
            continue
        elif curr == next:
            drop_count += 1
        elif curr < next:
            sum = 0
            target_idx = i
            for j in range(i, -1, -1):
                if inputs[j] < next:
                    sum += inputs[j]
                    if sum < next:
                       target_idx = j
                    else:
                        break
            drop_count += i - target_idx + 1

    print(f"drop_count: {drop_count}")

solution5()