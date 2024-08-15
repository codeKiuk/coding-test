def main():
    N = int(input())
    members = sorted(list(map(int, input().split())))

    accrue = 0
    result = 0

    for idx, member in enumerate(members):
        result += accrue + member
        accrue += member

    print(result)

main()