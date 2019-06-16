"""
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

what if you can't use division?
"""

def get_pre_products(numbers):
    l = len(numbers)
    pre_products = [1] * l
    for i in range(1, l):
        pre_products[i] =  pre_products[i - 1] * numbers[i - 1]
    return pre_products

def get_post_products(numbers):
    l = len(numbers)
    post_products = [1] * l
    for i in range(l - 2, -1, -1):
        post_products[i] =  post_products[i + 1] * numbers[i + 1]
    return post_products

def get_products(numbers):
    pre_products = get_pre_products(numbers)
    post_products = get_post_products(numbers)
    return [pre_products[i] * post_products[i] for i in range(len(numbers))]

if __name__ == "__main__":
    numbers = [int(x) for x in input().strip().split()]
    print(get_products(numbers))
    