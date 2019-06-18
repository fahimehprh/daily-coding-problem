"""
Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
"""
def is_string_valid(string):
    stack = []
    for char in string:
        if char == '[' or char == '{' or char == '(':
            stack.append(char)
        elif char == '}':
            if len(stack) == 0 or stack[-1] != '{':
                return False
            stack.pop()
        elif char == ')':
            if len(stack) == 0 or stack[-1] != '(':
                return False
            stack.pop()
        else:
            if len(stack) == 0 or stack[-1] != '[':
                return False
            stack.pop()
    if len(stack) != 0:
        return False
    return True

if __name__ == "__main__":
    string = input()
    print(is_string_valid(string))
    