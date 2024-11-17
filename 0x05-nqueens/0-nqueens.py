#!/usr/bin/python3
"""
N Queens problem
"""
import sys


def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen at board[row][col]
    on the board of size N x N.

    Parameters:
    - board (list): The current state of the chessboard.
    - row (int): The row index to check.
    - col (int): The column index to check.
    - N (int): The size of the board.

    Returns:
    - bool: True if it's safe to place a queen, otherwise False.
    """
    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col, N, solutions):
    """
    A recursive utility function to solve N Queens problem.

    Parameters:
    - board (list): The current state of the chessboard.
    - col (int): The current column index.
    - N (int): The size of the board.
    - solutions (list): List to store all possible solutions.

    Returns:
    - bool: True if a solution is found, otherwise False.
    """
    if col >= N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return True

    res = False
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1

            res = solve_nqueens_util(board, col + 1, N, solutions) or res

            board[i][col] = 0

    return res


def solve_nqueens(N):
    """
    Solves the N Queens puzzle for a board of size N x N.

    Parameters:
    - N (int): The size of the board.

    Prints:
    - All possible solutions to the N Queens problem in the desired format.
    """
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []

    if not solve_nqueens_util(board, 0, N, solutions):
        print("No solution exists for N =", N)
        sys.exit(1)

    for sol in solutions:
        print(sol)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        solve_nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
