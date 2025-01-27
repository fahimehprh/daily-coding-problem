"""

Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are integers and returns x^y.

Do this faster than the naive method of repeated multiplication.

For example, pow(2, 10) should return 1024.

"""

def pow(base, power):
    if power == 0:
        return 1
    
    if power % 2 == 0:
        return pow(base * base, power // 2)
    else:
        return pow(base * base, power // 2) * base


if __name__ == "__main__":
    print(pow(2, 10))
    print(pow(3, 2))
    print(pow(4, 3))
