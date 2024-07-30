import sys
def main():
    input = sys.stdin.readline  
    N = int(input())
    members = []
    for i in range(N):
        age, name = input().split()
        members.append((int(age), name, i))

    sorted_members = sorted(members, key=lambda x : (int(x[0]), x[2]) )

    for member in sorted_members:
        print(f"{member[0]} {member[1]}")


main()    