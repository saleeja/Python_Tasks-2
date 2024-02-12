"""4.Write a Python program to reverse a string"""


def reverse(text):
    return text[::-1]

"""Reverses the given string.

    Args:
        text: The string to reverse.

    Return:
        The reversed string.
"""
text=(input("Enter a word:"))
reverse= reverse(text)
print(reverse)