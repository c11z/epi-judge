from test_framework import generic_test
from binary_tree_node import BinaryTreeNode
from typing import Tuple

# use post order traversal, base case at empty child of leaf node sets height at -1
# tree if balanced if all sub trees are balanced
# O(n) time complexity -- have to visit every node to be sure
# O(h) space complexity -- recursive function stack size is height of the tree
def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    def balance(tree: BinaryTreeNode) -> Tuple[bool, int]:
        if not tree:
            return (True, -1)

        is_left_balanced, left_height = balance(tree.left)
        if not is_left_balanced:
            return (False, 0)
        is_right_balanced, right_height = balance(tree.right)
        if not is_right_balanced:
            return (False, 0)

        is_balanced = abs(left_height - right_height) <= 1
        height = max(left_height, right_height) + 1
        return (is_balanced, height)

    return balance(tree)[0]


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_tree_balanced.py", "is_tree_balanced.tsv", is_balanced_binary_tree
        )
    )
