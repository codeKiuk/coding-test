import sys
from itertools import combinations, permutations

def main():
    input = sys.stdin.readline

    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    all_team = list(range(1, N+1))
    team_member_num = N // 2
    answer = float('inf')

    def get_team_score(team):
        nonlocal answer


        link_team = list(set(all_team) - set(team))
        start_team_combi = list(permutations(team, 2))
        link_team_combi = list(permutations(link_team, 2))

        start_team_sum = 0
        link_team_sum = 0

        for start_team in start_team_combi:
            i, j = start_team
            start_team_sum += graph[i-1][j-1]

        for link_team in link_team_combi:
            i, j = link_team
            link_team_sum += graph[i-1][j-1]

        answer = min(answer, abs(start_team_sum - link_team_sum))

    def recursion(start_idx, team):

        if len(team) == team_member_num:
            get_team_score(team)
            return

        if start_idx == N+1:
            return
        
        for idx in range(start_idx, N+1):
            team.append(idx)
            recursion(idx+1, team)
            team.pop()


    recursion(2, [1])

    print(answer)

main()

"""
20
0 1 2 3 4 5 0 1 2 3 4 5 0 1 2 3 4 5 0 1
1 0 2 3 4 5 0 1 2 3 4 5 0 1 2 3 4 5 0 1
1 2 0 3 4 5 0 1 2 3 4 5 0 1 2 3 4 5 0 1
1 2 3 0 4 5 0 1 2 3 4 5 0 1 2 3 4 5 0 1
1 2 3 4 0 5 0 1 2 3 4 5 0 1 2 3 4 5 0 1
1 2 3 4 5 0 0 1 2 3 4 5 0 1 2 3 4 5 0 1
1 2 3 4 5 0 0 1 2 3 4 5 0 1 2 3 4 5 0 1
1 2 3 4 5 0 0 1 2 3 4 5 0 1 2 3 4 5 0 1
1 2 3 4 5 0 0 1 2 3 4 5 0 1 2 3 4 5 0 1
1 2 3 4 5 0 0 1 2 3 4 5 0 1 2 3 4 5 0 1
1 2 3 4 5 0 0 1 2 3 4 5 0 1 2 3 4 5 0 1
1 2 3 4 5 0 0 1 2 3 4 5 0 1 2 3 4 5 0 1
1 2 3 4 5 0 0 1 2 3 4 5 0 1 2 3 4 5 0 1
1 2 3 4 5 0 0 1 2 3 4 5 0 1 2 3 4 5 0 1
1 2 3 4 5 0 0 1 2 3 4 5 0 1 2 3 4 5 0 1
1 2 3 4 5 0 0 1 2 3 4 5 0 1 2 3 4 5 0 1
1 2 3 4 5 0 0 1 2 3 4 5 0 1 2 3 4 5 0 1
1 2 3 4 5 0 0 1 2 3 4 5 0 1 2 3 4 5 0 1
1 2 3 4 5 0 0 1 2 3 4 5 0 1 2 3 4 5 0 1
1 2 3 4 5 0 0 1 2 3 4 5 0 1 2 3 4 5 0 1
"""