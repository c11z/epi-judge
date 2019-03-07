import collections
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from typing import Tuple, Dict

# need to track the key: value pair for isbn: price
# need to track an order of when a key is utilized
# insert existing key ignores new price, just updates order
# if over capacity remove least used key
# O(1) all if properly modeled
class LruCache:
    def __init__(self, capacity: int) -> None:
        # store relation of isbn to price
        self.aux: Dict[int, int] = {}
        # list of isbn in order least to most recently used
        self.que: List[int] = []
        # memo capacity
        self.cap: int = capacity
        return None

    def lookup(self, isbn: int) -> int:
        if isbn in self.aux:
            self.que.remove(isbn)
            self.que.append(isbn)
        return self.aux.get(isbn, -1)

    def insert(self, isbn: int, price: int) -> None:
        if isbn in self.aux:
            self.que.remove(isbn)
            self.que.append(isbn)
        else:
            self.que.append(isbn)
            self.aux[isbn] = price
            if len(self.que) > self.cap:
                del self.aux[self.que.pop(0)]
        return None

    def erase(self, isbn: int) -> bool:
        if self.aux.get(isbn):
            del self.aux[isbn]
            self.que.remove(isbn)
            return True
        else:
            return False


# soltion from book
class LruCache:
    def __init__(self, capacity):

        self._isbn_price_table = collections.OrderedDict()
        self._capacity = capacity

    def lookup(self, isbn):

        if isbn not in self._isbn_price_table:
            return -1
        price = self._isbn_price_table.pop(isbn)
        self._isbn_price_table[isbn] = price
        return price

    def insert(self, isbn, price):

        # We add the value for key only if key is not present - we don't update
        # existing values.
        if isbn in self._isbn_price_table:
            price = self._isbn_price_table.pop(isbn)
        elif len(self._isbn_price_table) == self._capacity:
            self._isbn_price_table.popitem(last=False)
        self._isbn_price_table[isbn] = price

    def erase(self, isbn):

        return self._isbn_price_table.pop(isbn, None) is not None


def run_test(commands):
    if len(commands) < 1 or commands[0][0] != "LruCache":
        raise RuntimeError("Expected LruCache as first command")

    cache = LruCache(commands[0][1])

    for cmd in commands[1:]:
        if cmd[0] == "lookup":
            result = cache.lookup(cmd[1])
            if result != cmd[2]:
                raise TestFailure(
                    "Lookup: expected " + str(cmd[2]) + ", got " + str(result)
                )
        elif cmd[0] == "insert":
            cache.insert(cmd[1], cmd[2])
        elif cmd[0] == "erase":
            result = 1 if cache.erase(cmd[1]) else 0
            if result != cmd[2]:
                raise TestFailure(
                    "Erase: expected " + str(cmd[2]) + ", got " + str(result)
                )
        else:
            raise RuntimeError("Unexpected command " + cmd[0])


if __name__ == "__main__":
    exit(generic_test.generic_test_main("lru_cache.py", "lru_cache.tsv", run_test))
