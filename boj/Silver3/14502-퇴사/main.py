# 난 정말.. 완탐에 약하다. 엣지케이스에 정말 약해 정말 정말로... ㅜㅜ
def main():
    import sys
    input = sys.stdin.readline

    days = int(input())

    graph = [list(map(int, input().split()))+[current_day] for current_day in range(days)]
                    # (time, income, current_day)

    global max_income
    max_income = 0

    def dp(day, incomes):
        global max_income
        time, income, current_day = day
        print(f"current_day: {current_day}, time: {time}, income: {income}, incomes: {incomes}, max_income: {max_income}")

        if current_day>= days:
            max_income = max(max_income, incomes)

        elif time == 1:
            if current_day + time < days:
                max_income = max(max_income, dp(graph[current_day+1], incomes+income))
            if current_day + time == days:
                max_income = max(max_income, incomes+income)
        else:
            if current_day + time < days:
                                            # 상담한다                                      # 상담하지 않는다
                max_income = max(max_income, dp(graph[current_day+time], incomes+income), dp(graph[current_day+1], incomes))
            if current_day + time > days:
                if current_day + 1 < days:
                    max_income = max(max_income, dp(graph[current_day+1], incomes))
                if current_day + 1 == days:
                    max_income = max(max_income, incomes)
            if current_day + time == days:
                max_income = max(max_income, incomes+income, dp(graph[current_day+1], incomes))

        print('MAX INCOME: ', max_income)

        return max_income


    for i in range(days):
        print(f"DAY {i}")
        max_income = max(max_income, dp(graph[i], 0))

    print(max_income)

main()

"""
4
1 1
3 1
1 1
1 1
3

4
3 1
1 100
2 100
1 1000
1100

3
3 100
1 99
1 2
101

3
2 100
2 6
1 5
105

3
2 10
5 20
1 10
20

"""