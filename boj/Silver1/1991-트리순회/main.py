import sys
def main():
    input = sys.stdin.readline
    N = int(input())
    nodes = sorted([list(map(str, input().split())) for _ in range(N)])
    first_nodes = [node[0] for node in nodes]


    def pre_order(start_nodes=nodes[0]):
        nonlocal nodes
        print(start_nodes[0], end='')
        if start_nodes[1] != '.':
            pre_order(nodes[first_nodes.index(start_nodes[1])])
        if start_nodes[2] != '.':
            pre_order(nodes[first_nodes.index(start_nodes[2])])

    def in_order(start_nodes=nodes[0]):
        nonlocal nodes
        if start_nodes[1] != '.':
            in_order(nodes[first_nodes.index(start_nodes[1])])
        print(start_nodes[0], end='')
        if start_nodes[2] != '.':
            in_order(nodes[first_nodes.index(start_nodes[2])])

    def post_order(start_nodes=nodes[0]):
        nonlocal nodes
        if start_nodes[1] != '.':
            post_order(nodes[first_nodes.index(start_nodes[1])])
        if start_nodes[2] != '.':
            post_order(nodes[first_nodes.index(start_nodes[2])])
        print(start_nodes[0], end='')

    pre_order()
    print()
    in_order()
    print()
    post_order()
main()


