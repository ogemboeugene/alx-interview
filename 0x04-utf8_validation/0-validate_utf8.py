#!/usr/bin/python3
'''
Script that determines if a given data set represents a valid UTF-8 encoding
'''


def validUTF8(data):
    """
    Checks if a list of integers represents a valid UTF-8 encoding.

    Args:
    - data (list of int): List of integers representing 8-bit data bytes.

    Returns:
    - bool: True if data is a valid UTF-8 encoding, else return False.
    """

    skip = 0
    n = len(data)

    for i in range(n):
        if skip > 0:
            if data[i] >> 6 != 0b10:
                return False
            skip -= 1
            continue

        if type(data[i]) != int or data[i] < 0 or data[i] > 0x10ffff:
            return False

        elif data[i] <= 0x7f:
            skip = 0
        elif data[i] & 0b11111000 == 0b11110000:
            span = 4
            if n - i >= span:
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + span],
                ))
                if not all(next_body):
                    return False
                skip = span - 1
            else:
                return False
        elif data[i] & 0b11110000 == 0b11100000:
            span = 3
            if n - i >= span:
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + span],
                ))
                if not all(next_body):
                    return False
                skip = span - 1
            else:
                return False
        elif data[i] & 0b11100000 == 0b11000000:
            span = 2
            if n - i >= span:
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + span],
                ))
                if not all(next_body):
                    return False
                skip = span - 1
            else:
                return False
        else:
            return False

    return True
