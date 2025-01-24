import statistics
import math

"""
Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

2
1.5
2
3.5
2
2
2
"""

# def get_median(l):
#     return statistics.median(l)

def get_median(l):
    l.sort()
    first_middle, second_middle = math.floor((len(l) - 1) / 2), math.ceil((len(l) - 1) / 2)
    return (l[first_middle] + l[second_middle]) / 2
    


if __name__ == "__main__":

    list = [2, 1, 5, 7, 2, 0, 5]

    for i in range(len(list)):
        print(get_median(list[:i+1]))
