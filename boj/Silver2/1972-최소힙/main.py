def main():
    import sys
    input = sys.stdin.readline

    N = int(input())

    import heapq

    stack = []
    array = []
    heapq.heapify(array)

    for _ in range(N):
        command_or_input = int(input())

        if command_or_input == 0:
            if array:
                smallest = heapq.heappop(array)
                stack.append(smallest)
            else:
                stack.append(0)

        else:
            heapq.heappush(array, command_or_input)

    for element in stack:
        print(element)

main()