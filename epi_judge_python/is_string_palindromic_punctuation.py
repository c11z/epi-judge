from test_framework import generic_test


# O(n) time complexity O(1) space
def is_palindrome(s: str):
    i = 0
    j = len(s) - 1
    trip = True if s == "" else False
    while i < j:
        if not s[i].isalnum():
            i += 1
        elif not s[j].isalnum():
            j -= 1
        elif s[i].lower() == s[j].lower():
            trip = True
            i += 1
            j -= 1
        else:
            return False
    return trip


# solution from book
def is_palindrome(s):
    # i moves forward, and j moves backward.
    i, j = 0, len(s) - 1
    while i < j:
        # i and j both skip non-alphanumeric characters.
        while not s[i].isalnum() and i < j:
            i += 1
        while not s[j].isalnum() and i < j:
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i, j = i + 1, j - 1
    return True


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_string_palindromic_punctuation.py",
            "is_string_palindromic_punctuation.tsv",
            is_palindrome,
        )
    )
