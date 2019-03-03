import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook
from binary_tree_with_parent_prototype import BinaryTreeNode


# determine height of both nodes
# move lower node to same height as higher node
# move each node to parent in tandem until they match
# O(h) time complexity, where h is the depth of the deepst node
# O(1) space complexity, no recursive call stack, just memo heights
def lca(node0: BinaryTreeNode, node1: BinaryTreeNode) -> BinaryTreeNode:
    def height(node: BinaryTreeNode) -> int:
        n = 0
        while node.parent:
            n += 1
            node = node.parent
        return n

    height0 = height(node0)
    height1 = height(node1)
    
    # node0 is always shorter
    if height1 < height0:
        node0, node1 = node1, node0

    for _ in range(abs(height1 - height0)):
        node1 = node1.parent

    while node0 != node1:
        node0 = node0.parent
        node1 = node1.parent
    return node0

@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0), must_find_node(tree, node1))
    )

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "lowest_common_ancestor_with_parent.py",
            "lowest_common_ancestor.tsv",
            lca_wrapper,
        )
    )
