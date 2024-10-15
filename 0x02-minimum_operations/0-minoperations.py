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
    if n <= 1:
        return 0
    
    operations = 0
    factor = 2
    
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    
    return operations
