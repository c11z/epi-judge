from test_framework import generic_test
from list_node import ListNode

# Assumes L has at least k nodes, deletes the k-th last node in L.
# O(n) time complexity, O(1) space
def remove_kth_last(L: ListNode, k: int) -> None:
    dummy_head = front = back = ListNode(0, L)
    for _ in range(k):
        front = front.next

    while front.next:
        front = front.next
        back = back.next
    back.next = back.next.next
    return dummy_head.next


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "delete_kth_last_from_list.py",
            "delete_kth_last_from_list.tsv",
            remove_kth_last,
        )
    )
