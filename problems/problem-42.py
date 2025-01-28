"""
Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. If such a subset cannot be made, then return null.

Integers can appear more than once in the list. You may assume all numbers in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.
"""


def subset_sum(s, k):
    if s == [] or k < 0:
        return None
    
    if s[0] == k:
        return [s[0]]
    
    smaller_subset = subset_sum(s[1:], k - s[0])
    if smaller_subset is not None:
        return smaller_subset + [s[0]]
    
    return subset_sum(s[1:], k)
    


if __name__ == "__main__":
    print(subset_sum([12, 1, 61, 5, 9, 2], 12))
    print(subset_sum([12, 1, 61, 5, 9, 2], 2))
    print(subset_sum([12, 1, 61, 5, 9, 2], 10))
    print(subset_sum([12, 1, 61, 5, 9, 2], 24))
