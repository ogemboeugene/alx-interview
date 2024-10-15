#!/usr/bin/python3
'''
Simple script to calculate the minimum number of operations needed to obtain
n 'H' characters using the operations Copy All and Paste.
'''


def minOperations(n):
    '''
    Calculate the minimum number of operations needed to obtain
    n 'H' characters using the operations Copy All and Paste.
    '''
    if n == 1:
        return 0  # No operations needed for a single 'H'

    dp = [float('inf')] * (n + 1)
    dp[1] = 0

    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[n] if dp[n] != float('inf') else 0
