#!/usr/bin/python3
"""Task 0 Module -2D matrix rotation
"""


def rotate_2d_matrix(matrix):
    """Rotates an m by n 2D matrix in place.
    """
    if type(matrix) != list:
        return
    if len(matrix) <= 0:
        return
    if not all(map(lambda x: type(x) == list, matrix)):
        return

    rows = len(matrix)
    cols = len(matrix[0])

    if not all(map(lambda x: len(x) == cols, matrix)):
        return

    co, ro = 0, rows - 1

    for i in range(cols * rows):
        if i % rows == 0:
            matrix.append([])
        if ro == -1:
            ro = rows - 1
            co += 1

        matrix[-1].append(matrix[ro][co])

        if co == cols - 1 and ro >= -1:
            matrix.pop(ro)
        ro -= 1
