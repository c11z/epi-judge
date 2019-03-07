from typing import List
from test_framework import generic_test


# the key is the track the index of each word in a dict
# then when a duplicate word is found you can derive the distance
# by subtracting from the current index
# then just keep track of the minimum
# O(n) time complexity where n is number of words in the paragraph
# O(L) extra space where L is the number of unique words
def find_nearest_repetition(paragraph: List[str]) -> int:
    minimum: int = len(paragraph) + 1
    memo: Dict[str, int] = {}
    for index, word in enumerate(paragraph):
        if word in memo:
            minimum = min(minimum, index - memo[word])
            # update word index in case the word shows up again
            memo[word] = index
        else:
            memo[word] = index
    return -1 if minimum == len(paragraph) + 1 else minimum


# soltion from book
def find_nearest_repetition(paragraph):
    word_to_latest_index, nearest_repeated_distance = {}, float("inf")
    for i, word in enumerate(paragraph):
        if word in word_to_latest_index:
            latest_equal_word = word_to_latest_index[word]
            nearest_repeated_distance = min(
                nearest_repeated_distance, i - latest_equal_word
            )
        word_to_latest_index[word] = i
    return (
        nearest_repeated_distance if nearest_repeated_distance != float("inf") else -1
    )


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "nearest_repeated_entries.py",
            "nearest_repeated_entries.tsv",
            find_nearest_repetition,
        )
    )
