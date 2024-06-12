"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""


def decode_ways(s):

    if not s:
        return 1

    if len(s) == 1 and s[0] != "0":
        return 1

    if int(s[:2]) <= 26:
        return decode_ways(s[1:]) + decode_ways(s[2:])

    return decode_ways(s[1:])


if __name__ == "__main__":
    s = "111"
    print(decode_ways(s))
