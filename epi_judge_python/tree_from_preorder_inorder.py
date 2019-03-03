from test_framework import generic_test
from typing import List, Optional
from binary_tree_node import BinaryTreeNode


# solution from book
def binary_tree_from_preorder_inorder(preorder, inorder):

    node_to_inorder_idx = {data: i for i, data in enumerate(inorder)}

    # Builds the subtree with preorder[preorder_start:preorder_end] and
    # inorder[inorder_start:inorder_end].
    def binary_tree_from_preorder_inorder_helper(
        preorder_start, preorder_end, inorder_start, inorder_end
    ):
        if preorder_end <= preorder_start or inorder_end <= inorder_start:
            return None

        root_inorder_idx = node_to_inorder_idx[preorder[preorder_start]]
        left_subtree_size = root_inorder_idx - inorder_start
        return BinaryTreeNode(
            preorder[preorder_start],
            # Recursively builds the left subtree.
            binary_tree_from_preorder_inorder_helper(
                preorder_start + 1,
                preorder_start + 1 + left_subtree_size,
                inorder_start,
                root_inorder_idx,
            ),
            # Recursively builds the right subtree.
            binary_tree_from_preorder_inorder_helper(
                preorder_start + 1 + left_subtree_size,
                preorder_end,
                root_inorder_idx + 1,
                inorder_end,
            ),
        )

    return binary_tree_from_preorder_inorder_helper(0, len(preorder), 0, len(inorder))


# O(n) time complexity to build the dict and make each node
# O(n) space complexity to store the dict and the recursive stack
def binary_tree_from_preorder_inorder(
    preorder: List[int], inorder: List[int]
) -> BinaryTreeNode:
    inorder_idx = {d: i for i, d in enumerate(inorder)}

    def loop(
        po_start: int, po_end: int, io_start: int, io_end: int
    ) -> Optional[BinaryTreeNode]:
        if po_end <= po_end and io_end <= io_start:
            return None
        root_idx = inorder_idx[preorder[po_start]]
        left_subtree_size = root_idx - io_start
        return BinaryTreeNode(
            preorder[po_start],
            loop(po_start + 1, po_start + 1 + left_subtree_size, io_start, root_idx),
            loop(po_start + 1 + left_subtree_size, po_end, root_idx + 1, io_end),
        )

    return loop(0, len(preorder), 0, len(inorder))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "tree_from_preorder_inorder.py",
            "tree_from_preorder_inorder.tsv",
            binary_tree_from_preorder_inorder,
        )
    )
