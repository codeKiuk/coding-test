def main():
    import sys
    input = sys.stdin.readline

    trees = dict()
    count = 0

    while True:
        user_input = input()
        if len(user_input) <= 1:
            break

        count += 1

        # dict in => O(1)
        if user_input in trees:
            trees[user_input] += 1
        else:
            trees[user_input] = 1
        
        
    sorted_trees = sorted(trees.items())
    for tree in sorted_trees:
        tree_name, tree_count = tree
        strip_tree_name = tree_name.strip('\n')
        print(f"{strip_tree_name} {(tree_count / count * 100):.4f}")



main()