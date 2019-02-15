from test_framework import generic_test
from test_framework.test_failure import TestFailure
from collections import namedtuple


# O(1) time and O(n) space
class Stack:
    Item = namedtuple("Item", ("value", "max"))

    def __init__(self) -> None:
        self._stack = []
        return None

    def empty(self) -> bool:
        return len(self._stack) == 0

    def max(self) -> int:
        if self.empty():
            raise Exception("no max in empty stack")
        return self._stack[-1].max

    def pop(self) -> int:
        return self._stack.pop().value

    def push(self, x: int) -> None:
        self._stack.append(self.Item(x, x if self.empty() else max(x, self.max())))
        return


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == "Stack":
                s = Stack()
            elif op == "push":
                s.push(arg)
            elif op == "pop":
                result = s.pop()
                if result != arg:
                    raise TestFailure(
                        "Pop: expected " + str(arg) + ", got " + str(result)
                    )
            elif op == "max":
                result = s.max()
                if result != arg:
                    raise TestFailure(
                        "Max: expected " + str(arg) + ", got " + str(result)
                    )
            elif op == "empty":
                result = int(s.empty())
                if result != arg:
                    raise TestFailure(
                        "Empty: expected " + str(arg) + ", got " + str(result)
                    )
            else:
                raise RuntimeError("Unsupported stack operation: " + op)
    except IndexError:
        raise TestFailure("Unexpected IndexError exception")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "stack_with_max.py", "stack_with_max.tsv", stack_tester
        )
    )
