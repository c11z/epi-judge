from test_framework import generic_test
from binary_tree_with_parent_prototype import BinaryTreeNode
from typing import List

# start at root, track each node on every level, add their data to the result
# then replace them with the children of those nodes
# O(n) time and O(M) space complexity where n is the number of nodes
# and m is the largest number of nodes on a level
def binary_tree_depth_order(tree: BinaryTreeNode) -> List[int]:
    result = []
    if not tree:
        return result
    level = [tree]
    while level:
        result.append([node.data for node in level])
        level = [child for node in level for child in (node.left, node.right) if child]
    return result


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "tree_level_order.py", "tree_level_order.tsv", binary_tree_depth_order
        )
    )
