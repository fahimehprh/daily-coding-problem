"""
Given a string s and an integer k, break up the string into multiple lines such that each line has a length of k or less. You must break it up so that words don't break across lines. Each line has to have the maximum possible amount of words. If there's no way to break the text up, then return null.

You can assume that there are no spaces at the ends of the string and that there is exactly one space between each word.

For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10, you should return: ["the quick", "brown fox", "jumps over", "the lazy", "dog"]. No string in the list has a length of more than 10.
"""


def break_string(s, k):
    words = s.split(" ")

    if any([len(w) > k for w in words]):
        print(None, '\n')
        return
    
    current_line = words[0]
    for w in words[1:]:
        if len(current_line) + len(w) + 1 > k:
            print(current_line)
            current_line = w
        else:
            current_line += ' ' + w
    
    print(current_line)
    print()


if __name__ == "__main__":
    break_string("the quick brown fox jumps over the lazy dog", 10)
    break_string("thequick brown fox jumps over the lazy dog", 10)
    break_string("thequickbrownfox jumps over the lazy dog", 10)
    break_string("the quick", 10)
    break_string("the", 10)
