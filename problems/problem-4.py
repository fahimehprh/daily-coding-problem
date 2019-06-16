"""
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""

def check_index(index, numbers, start_index):
    l = len(numbers)
    if index < 0 or index > l-1 or numbers[index] == '*':
        return
    value = numbers[index] - 1
    if index != start_index:
        check_index(value, numbers, start_index)
    numbers[index] = '*'

def get_min_num(numbers):
    l = len(numbers)
    for i in range(l):
        if numbers[i] != '*':
            check_index(numbers[i] - 1, numbers, i)
    for i in range(l):
        if numbers[i] != '*':
            return i + 1
    return l

if __name__ == "__main__":
    numbers = [int(x) for x in input().strip().split()]
    print(get_min_num(numbers))
    