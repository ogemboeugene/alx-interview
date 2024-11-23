#!/usr/bin/python3
"""
Rotate matrix
"""


def rotate_2d_matrix(matrix) -> None:
    """
    Rotates a 2D square matrix by 90 degrees clockwise.
    Args:
    matrix (list[list]): The input matrix to be rotated.
    Returns:
    None; the function modifies the input matrix in-place.
    """
    n = len(matrix)

    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - j - 1][i]
            matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
            matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
            matrix[j][n - i - 1] = temp
