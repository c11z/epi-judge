import functools
from list_node import ListNode
from typing import Optional, Set
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

# assumes all nodes have unique data
# records seen data values in a set
# O(n) time complexity and O(n) extra space
def has_cycle(head: ListNode) -> Optional[ListNode]:
    seen: Set[int] = set()
    i = head
    while i.next:
        i = i.next
        if i.data in seen:
            return i
        seen.add(i.data)
    return None


# two loop method, track outer loop count n
# inner loop loops n time
# track how many time inner loop visits outerloop
# time complexity O(n^2) but O(1) space
def has_cycle(head: ListNode) -> Optional[ListNode]:
    i: ListNode = head
    n: int = 0
    while i.next:
        i = i.next
        n += 1
        visit: int = 0
        j: ListNode = head
        for _ in range(n):
            if j.data == i.data:
                visit += 1
                if visit == 2:
                    return i
            j = j.next
    return None


# fast slow method
# verify there is a cycle by running two indexes
# slow takes one step, fast takes two
# if there is a cycle then fast will wrap and catch slow
# otherwise fast will be None
# once a cycle is found, count the steps unti fast meets slow again
# then to find the beginning of the cycle set a front and back index
# a cycle length apart and move them at the same time until they match
# O(n) time complexity and O(1) space
def has_cycle(head: ListNode) -> Optional[ListNode]:
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if slow.data == fast.data:
            fast = fast.next
            cycle_length: int = 1
            while slow.data != fast.data:
                fast = fast.next
                cycle_length += 1
            front = back = head
            for _ in range(cycle_length):
                front = front.next
            while back.data != front.data:
                front = front.next
                back = back.next
            return back

    return None


# solution from book
def has_cycle(head):
    def cycle_len(end):
        start, step = end, 0
        while True:
            step += 1
            start = start.next
            if start is end:
                return step

    fast = slow = head
    while fast and fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            # Finds the start of the cycle.
            cycle_len_advanced_iter = head
            for _ in range(cycle_len(slow)):
                cycle_len_advanced_iter = cycle_len_advanced_iter.next

            it = head
            # Both iterators advance in tandem.
            while it is not cycle_len_advanced_iter:
                it = it.next
                cycle_len_advanced_iter = cycle_len_advanced_iter.next
            return it  # iter is the start of cycle.
    return None  # No cycle.


# better version from the book
# doesn't require to count cycle length
# assumes that fast will  always catch slow at the end of the cycle
# and so resetting slow to head and walking in tandem will find the beginning of the cycle
# it works!
def has_cycle(head: ListNode) -> Optional[ListNode]:
    slow = fast = head
    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if slow.data == fast.data:
            slow = head
            while slow.data != fast.data:
                slow = slow.next
                fast = fast.next
            return slow
    return None


@enable_executor_hook
def has_cycle_wrapper(executor, head, cycle_idx):
    cycle_length = 0
    if cycle_idx != -1:
        if head is None:
            raise RuntimeError("Can't cycle empty list")
        cycle_start = None
        cursor = head
        while cursor.next is not None:
            if cursor.data == cycle_idx:
                cycle_start = cursor
            cursor = cursor.next
            cycle_length += 1 if cycle_start is not None else 0

        if cursor.data == cycle_idx:
            cycle_start = cursor
        if cycle_start is None:
            raise RuntimeError("Can't find a cycle start")
        cursor.next = cycle_start
        cycle_length += 1

    result = executor.run(functools.partial(has_cycle, head))

    if cycle_idx == -1:
        if result is not None:
            raise TestFailure("Found a non-existing cycle")
    else:
        if result is None:
            raise TestFailure("Existing cycle was not found")
        cursor = result
        while True:
            cursor = cursor.next
            cycle_length -= 1
            if cursor is None or cycle_length < 0:
                raise TestFailure(
                    "Returned node does not belong to the cycle or is not the closest node to the head"
                )
            if cursor is result:
                break

    if cycle_length != 0:
        raise TestFailure(
            "Returned node does not belong to the cycle or is not the closest node to the head"
        )


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_list_cyclic.py", "is_list_cyclic.tsv", has_cycle_wrapper
        )
    )
