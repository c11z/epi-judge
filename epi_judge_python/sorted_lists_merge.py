from test_framework import generic_test
from list_node import ListNode

# return the head.next of a new list, so keep track of that
# worst case time complexity is O(n + m) where we have to examine every element in both lists
# best case is O(1) where one of the lists is empty and we just point the head to the other list
def merge_two_sorted_lists(L1: ListNode, L2: ListNode) -> ListNode:
    head: ListNode = ListNode()
    tail: ListNode = head
    while L1 and L2:
        if L1.data < L2.data:
            tail.next = L1
            L1 = L1.next
        else:
            tail.next = L2
            L2 = L2.next
        tail = tail.next
    tail.next = L1 or L2
    return head.next


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sorted_lists_merge.py", "sorted_lists_merge.tsv", merge_two_sorted_lists
        )
    )
