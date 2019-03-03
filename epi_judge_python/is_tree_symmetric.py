from test_framework import generic_test
from binary_tree_node import BinaryTreeNode

# visit and compare the mirror value of each subtree
# O(n) time complexity
# O(h) space complexity
def is_symmetric(tree: BinaryTreeNode) -> bool:
    def check_symmetry(subtree0: BinaryTreeNode, subtree1: BinaryTreeNode) -> True:
        if subtree0 is None and subtree1 is None:
            return True
        elif subtree0 and subtree1:
            if subtree0.data == subtree1.data:
                return check_symmetry(subtree0.left, subtree1.right) and check_symmetry(
                    subtree0.right, subtree1.left
                )
        # subtrees do not equal one another
        return False

    if tree is None:
        return True
    else:
        return check_symmetry(tree.left, tree.right)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_tree_symmetric.py", "is_tree_symmetric.tsv", is_symmetric
        )
    )
