from collections import Counter
from test_framework import generic_test


# assumes that white space might be present and mess up counter init
# use subtract method which carries overflow as negative
# then walk through and make sure there are no negative counts
# could have just subtracted, although how would you know that?
# O(n + m) time complexity where n and m are the length of the texts
# O(L) extra space where L is the number of unique characters
def is_letter_constructible_from_magazine(letter_text: str, magazine_text: str) -> bool:
    mag: Counter = Counter(magazine_text.replace(" ", ""))
    let: Counter = Counter(letter_text.replace(" ", ""))
    mag.subtract(let)
    for remain in mag.values():
        if remain < 0:
            return False
    return True


def is_letter_constructible_from_magazine(letter_text, magazine_text):

    # Compute the frequencies for all chars in letter_text.
    char_frequency_for_letter = Counter(letter_text)

    # Checks if characters in magazine_text can cover characters in
    # char_frequency_for_letter.
    for c in magazine_text:
        if c in char_frequency_for_letter:
            char_frequency_for_letter[c] -= 1
            if char_frequency_for_letter[c] == 0:
                del char_frequency_for_letter[c]
                if not char_frequency_for_letter:
                    # All characters for letter_text are matched.
                    return True

    # Empty char_frequency_for_letter means every char in letter_text can be
    # covered by a character in magazine_text.
    return not char_frequency_for_letter


# Pythonic solution that exploits collections.Counter. Note that the
# subtraction only keeps keys with positive counts.
def is_letter_constructible_from_magazine_pythonic(letter_text, magazine_text):
    return not Counter(letter_text) - Counter(magazine_text)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_anonymous_letter_constructible.py",
            "is_anonymous_letter_constructible.tsv",
            is_letter_constructible_from_magazine,
        )
    )
