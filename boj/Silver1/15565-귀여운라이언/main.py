import sys
def main():
    input = sys.stdin.readline

    N, K = map(int, input().split())
    dolls = list(map(int, input().split()))

    start = 0
    end = 0
    answer = float('inf')

    if dolls[0] == 1 and K == 1:
        print(1)
        return

    end += 1
    from collections import Counter
    counter = Counter(dolls[start:end+1])
    if not counter[1]:
        counter[1] = 0
    if not counter[2]:
        counter[2] = 0
        
    while end < N:
        if counter[1] >= K:
            answer = min(answer, end - start + 1)
            counter[dolls[start]] -= 1
            start += 1
            continue
        end += 1
        if end < N:
            counter[dolls[end]] += 1

    print(answer if answer != float('inf') else -1)

main()