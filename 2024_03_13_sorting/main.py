# 두 배열의 원소 교체 문제
#  N, K 와 배열 A, B가 주어진다
# 최대 K번 바꿔치기 하여 배열 A의 모든 원소의 합이 최대가 되도록 한다
def solution1():
    n, k = map(int, input().split())
    array_a = list(map(int, input().split()))
    array_b = list(map(int, input().split()))

    array_a.sort(reverse=True) # 내림차순 정렬 
    array_b.sort(reverse=True)

    target_array_a = n -1
    target_array_b = 0

    while k > 0:
        if array_a[target_array_a] >= array_b[target_array_b]:
            break
        
        array_a[target_array_a], array_b[target_array_b] = array_b[target_array_b], array_a[target_array_a]

        target_array_a -= 1
        target_array_b += 1
        k -= 1
    
    print("RESULT: ", sum(array_a))

solution1()