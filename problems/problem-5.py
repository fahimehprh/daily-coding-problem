"""
Problem:

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last
element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4))
returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
"""


def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(pair):
    first = lambda a, b: a
    return pair(first)


def cdr(pair):
    last = lambda a, b: b
    return pair(last)

if __name__ == "__main__":
    print(car(cons(3, 4)))
    print(cdr(cons(3, 4)))
