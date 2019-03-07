from test_framework import generic_test
from typing import Dict, Set
import collections

# create a frequency count of unique characters
# walk though counts, fail if more than one odd count
# O(n) time complexity, where n in the number of characters in s
# O(m) space complexity where m is the number of unique characters
def can_form_palindrome(s: str) -> bool:
    freq: Dict[str, int] = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    # only one odd character is allowed
    # track with this bool
    is_odd = False
    for count in freq.values():
        if count % 2 != 0:
            if not is_odd:
                is_odd = True
            else:
                # more than one odd character
                # this cannot be a palindrome
                return False
    return True


# an even cleverer solution
# just track odd characters in a set
def can_form_palindrome(s: str) -> bool:
    singles: Set[str] = set([])
    for char in s:
        if char in singles:
            singles.remove(char)
        else:
            singles.add(char)
    return len(singles) < 2


# soltion from book
def can_form_palindrome(s):
    # A string can be permuted to form a palindrome if and only if the number
    # of chars whose frequencies is odd is at most 1.
    return sum(v % 2 for v in collections.Counter(s).values()) <= 1


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_string_permutable_to_palindrome.py",
            "is_string_permutable_to_palindrome.tsv",
            can_form_palindrome,
        )
    )
