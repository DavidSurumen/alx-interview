#!/usr/bin/python3
"""
Module for working with lockboxes.
"""


def canUnlockAll(boxes):
    """
    checks whether all boxes in a list of boxes can be opened,
    given that the first box is unlocked, and each box may
    contain keys to the other boxes.
    """
    # boxes are numbered from 0 to n - 1
    # 'boxes' is a list of lists
    # a key with the same number as a box opens that box
    posn = 0
    unlocked = {}

    for index in range(len(boxes)):

        if len(boxes[index]) == 0 or index == 0:
            unlocked[index] = "unlocked"

        for key in boxes[index]:
            if key < len(boxes) and key != index:
                unlocked[key] = key

        if len(unlocked) == len(boxes):
            return True
    return False
