"""
Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.
"""

def incode_string(inp):
    l = len(inp)
    cur_char = inp[0]
    cur_char_count = 1
    incoded = ''
    if l == 1:
        return('1' + inp)
    for i in range(1, l):
        if inp[i -1] != inp[i]:
            incoded += str(cur_char_count) + cur_char
            cur_char = inp[i]
            cur_char_count = 1
        else:
            cur_char_count += 1
    incoded += str(cur_char_count) + cur_char
    return incoded

def decode_string(inp):
    l = len(inp)
    decoded = ''
    cur_count = ''
    for i in range(l):
        if inp[i] >= '0' and inp[i] <= '9':
            cur_count += inp[i]
        else:
            decoded += inp[i] * int(cur_count)
            cur_count = ''
    return(decoded)

if __name__ == "__main__":
    inp = input()
    print(incode_string(inp))
    print(decode_string(incode_string(inp)))
