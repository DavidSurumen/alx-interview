#!/usr/bin/env python3
"""
This module defines the function 'pascal_triangle'
"""
def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal's triangle of n
    """
    if n <= 0:
        return []
    pasca = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            if i - 1 == 0:
                break
            row.append(pasca[i - 1][j - 1] + pasca[i - 1][j])
        row.append(1)
        pasca.append(row)

    return pasca
