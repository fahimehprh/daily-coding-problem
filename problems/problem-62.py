"""
There is an N by M matrix of zeroes. Given N and M, write a function to count the number of ways of starting at the top-left corner and getting to the bottom-right corner. You can only move right or down.

For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:

Right, then down
Down, then right
Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.
"""


import math


def count_ways(n, m):
    return math.comb(n + m - 2, n - 1)


if __name__ == "__main__":
    print(count_ways(5, 5))
    print(count_ways(2, 2))
    print(count_ways(3, 4))
