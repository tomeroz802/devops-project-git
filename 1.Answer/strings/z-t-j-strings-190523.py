"""With this string:
'monty pythons flying circus'
Create a function that returns a sorted string with no duplicate characters
(keep any whitespace):
Example: ' cfghilmnoprstuy'
Create a function that returns the words in reverse order:
Example: ['circus', 'flying', 'pythons', 'monty']
Create a function that returns a list of 4 character strings:
Example: ['mont', 'y py', 'thon', 's fl', 'ying', ' cir', 'cus']
### git comment
"""
import pytest


def no_duplicates(a_string):
    # Remove duplicates using a set, excluding whitespace
    unique_chars = set(a_string.replace(" ", " "))
    # Sort the unique characters
    sorted_chars = sorted(unique_chars)
    # Join the sorted characters into a string, preserving whitespace
    sorted_string = ''.join(sorted_chars)
    return sorted_string
    pass


def reversed_words(a_string):
    # Split the sentence into words
    words = a_string.split()
    # Reverse the order of the words
    reversed_words = words[::-1]
    return reversed_words
    pass


def four_char_strings(a_string):
    # Remove any leading or trailing spaces from the input string
    input_string = a_string.strip()
    # Create a list to store the 4-character strings
    four_char_strings = []
    # Iterate over the input string, extracting 4-character substrings
    i = 0
    while i < (len(input_string)):
        four_char_strings.append(input_string[i:i + 4])
        i = i + 4

    return four_char_strings
    pass


def test_no_duplicates():
    s = 'monty pythons flying circus'
    assert no_duplicates(s) == ' cfghilmnoprstuy'


def test_reversed_words():
    s = 'monty pythons flying circus'
    assert reversed_words(s) == ['circus', 'flying', 'pythons', 'monty']


def test_four_char_strings():
    s = 'monty pythons flying circus'
    assert four_char_strings(s) == ['mont', 'y py', 'thon', 's fl', 'ying', ' cir', 'cus']


def main():
    return pytest.main(__file__)


if __name__ == '__main__':
    main()
