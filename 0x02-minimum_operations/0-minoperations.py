#!/usr/bin/python3
"""
Task 0 - Module that defines the function minOperations
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly 'n'
    characters in a file.
    - The file has a single character.
    - It has only two possible operations, Copy All and Paste.

    Args:
        n -> number of characters required.

    Return:
        ops -> the number of operations
    """
    clipboard = 0
    ops = 0
    chars = 1

    while chars < n:
        if clipboard == 0:
            clipboard = chars
            chars += clipboard
            ops = 2

        elif (n - chars) % chars == 0:
            clipboard = chars
            chars += clipboard
            ops += 2

        else:
            chars += clipboard
            ops += 1

    return ops
