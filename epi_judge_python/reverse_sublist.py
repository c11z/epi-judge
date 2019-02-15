from test_framework import generic_test
from list_node import ListNode


# O(final) time complexity is dominated by the search for the finish node
def reverse_sublist(L: ListNode, start: int, finish: int) -> ListNode:
    dummy_head = sublist_head = ListNode(0, L)

    for _ in range(1, start):
        sublist_head = sublist_head.next

    sublist_iter = sublist_head.next
    for _ in range(finish - start):
        temp = sublist_iter.next
        sublist_iter.next = temp.next
        temp.next = sublist_head.next
        sublist_head.next = temp

    return dummy_head.next


def reverse_list(L: ListNode):
    h = ListNode(0, L)

    i = h.next
    while i.next:
        t = i.next
        i.next = t.next
        t.next = h.next
        h.next = t
    return h.next


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "reverse_sublist.py", "reverse_sublist.tsv", reverse_sublist
        )
    )
