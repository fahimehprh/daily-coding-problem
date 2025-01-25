
"""
Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in the matrix by going left-to-right, or up-to-down.

For example, given the following matrix:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]
"""


def get_col(matrix, col):
    return map(lambda x : x[col], matrix)


def search_for(matrix, word):
    possible_string = []

    for i in range(len(matrix)):
        possible_string.append(''.join(matrix[i][:]))

    for i in range(len(matrix[0])):
        possible_string.append(''.join(get_col(matrix, i)))

    return any([True for s in possible_string if s.find(word) != -1])
    

if __name__ == "__main__":
    matrix = [['F', 'A', 'C'],
        ['O', 'B', 'Q'],
        ['A', 'N', 'O'],
        ['M', 'A', 'S']]
    
    print(search_for(matrix,"FOAM"))
    print(search_for(matrix, "MASS"))
