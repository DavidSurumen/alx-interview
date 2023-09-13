#!/usr/bin/python3
"""
N Queens puzzle solution module
"""
import sys


global N


solutions = []


def saveSolution(board):
    """
    Utility function to save already found solutions for queens'
    placement.

    board (List): NxN matrix representing the chess board.
    """
    sol = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                sol.append([i, j])
    solutions.append(sol)
    return solutions


def isSafe(board, row, col):
    """
    Utility function to check if a queen can be placed on board[row][col].

    Description: This function is called when "col" queens are already placed
                 in columns from 0 to col - 1, so we need to check only the
                 left side for attacking queens.

    board (List): NxN matrix representing the chess board.
    row (int):    the row number for placing the queen.
    col (int):    the column number for placing the queen.

    Return (bool): False if queen cannot be placed in given row and column,
                   otherwise True
    """
    # check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solveUtil(board, col):
    """
    Utility function that carries out the placement of the queens in a
    chess board.

    board (List): NxN matrix that represents the chess board.
    col   (int):  the column number for placing each queen.

    Return (bool): True is all the queens have been placed successfully,
                   otherwise False.
    """
    # Base case: if all queens are placed, return true
    if col >= N:
        return True

    solved = False
    # Consider this column and trying placing this queen in all rows one by one
    for row in range(N):
        if isSafe(board, row, col):
            # Place this queen in board[row][col]
            board[row][col] = 1

            # Recur to place rest of the queens
            if solveUtil(board, col + 1):
                if row == N-1:
                    return True
                elif col == 0:
                    saveSolution(board)
                    solved = True
                    board = [[0 for _ in range(N)] for _ in range(N)]
                else:
                    return True

            # If placing queen in board[row][col] doesn't lead to a solution,
            # backtrack from board[row][col]
            board[row][col] = 0

    # If the queen cannot be placed in any row in this column col
    # then return false. Return true if a previous solution had been found
    if solved:
        return True
    return False


def nqueens():
    """
    This function solves the N Queens problem using backtracking.

    Description:  It uses solveUtil() utility function to solve the problem,
                  which places queens in the form of 1s.

    Return (bool): False if queens cannot be placed, otherwise returs True.
    """
    board = [[0 for _ in range(N)] for _ in range(N)]

    if not solveUtil(board, 0):
        print('solution does not exist')
        return False
    return True


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    N = sys.argv[1]

    try:
        N = eval(N)
    except Exception:
        print("N must be a number")
        exit(1)

    if N < 4:
        print("N must be at least 4")
        exit(1)

    if nqueens():
        for i in solutions:
            print(i)
