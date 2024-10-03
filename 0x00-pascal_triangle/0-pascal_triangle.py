#!/usr/bin/python3
"""
Pascal's Triangle Generator
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.

    Parameters:
        n (int): The number of rows to generate.

    Returns:
        list of lists: A list containing lists representing each row of
                        Pascal's Triangle.
                        Returns an empty list if n is less than or equal to 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle
