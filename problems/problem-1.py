"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""

def pairs_sum(numbers, k):
    l = len(numbers)
    for i in range(l):
        for j in range(i):
            if k == numbers[i] + numbers[j]:
                return True
    return False

if __name__ == "__main__":
    numbers = [int(x) for x in input().strip().split()]
    k = int(input().strip())
    print(pairs_sum(numbers, k))
    