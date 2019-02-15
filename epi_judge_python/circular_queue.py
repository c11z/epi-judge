from test_framework import generic_test
from test_framework.test_failure import TestFailure
from typing import List, Optional


# circlular queue using list and three indexes
# O(1) enqueue time
# O(1) amortized dequeue time accounting for dynamic resizing
class Queue:
    SCALE_FACTOR: int = 2

    def __init__(self, capacity: int) -> None:
        self._queue: List[Optional[int]] = [None] * capacity
        self._size: int = 0
        self._head: int = 0
        self._tail: int = 0
        return

    def enqueue(self, i: int) -> None:
        if self._tail == len(self._queue):
            self._queue = self._queue[self._head :] + self._queue[: self._head]
            self._head = 0
            self._tail = self._size
            self._queue += [None] * (
                (len(self._queue) * self.SCALE_FACTOR) - len(self._queue)
            )
        self._queue[self._tail] = i
        self._tail = self._tail + 1
        self._size += 1
        return None

    def dequeue(self) -> int:
        if self._size == 0:
            raise Exception("queue is empty")
        i = self._queue[self._head]
        self._head = self._head + 1
        self._size -= 1
        return i

    def size(self) -> int:
        return self._size


# solution from book
class Queue:

    SCALE_FACTOR = 2

    def __init__(self, capacity):

        self._entries = [None] * capacity
        self._head = self._tail = self._num_queue_elements = 0

    def enqueue(self, x):

        if self._num_queue_elements == len(self._entries):  # Needs to resize.
            # Makes the queue elements appear consecutively.
            self._entries = self._entries[self._head :] + self._entries[: self._head]
            # Resets head and tail.
            self._head, self._tail = 0, self._num_queue_elements
            self._entries += [None] * (
                len(self._entries) * Queue.SCALE_FACTOR - len(self._entries)
            )

        self._entries[self._tail] = x
        self._tail = (self._tail + 1) % len(self._entries)
        self._num_queue_elements += 1

    def dequeue(self):

        if not self._num_queue_elements:
            raise IndexError("empty queue")
        self._num_queue_elements -= 1
        result = self._entries[self._head]
        self._head = (self._head + 1) % len(self._entries)
        return result

    def size(self):

        return self._num_queue_elements


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == "Queue":
            q = Queue(arg)
        elif op == "enqueue":
            q.enqueue(arg)
        elif op == "dequeue":
            result = q.dequeue()
            if result != arg:
                raise TestFailure(
                    "Dequeue: expected " + str(arg) + ", got " + str(result)
                )
        elif op == "size":
            result = q.size()
            if result != arg:
                raise TestFailure("Size: expected " + str(arg) + ", got " + str(result))
        else:
            raise RuntimeError("Unsupported queue operation: " + op)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "circular_queue.py", "circular_queue.tsv", queue_tester
        )
    )
