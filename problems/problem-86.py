def remove_to_valid(string):
    starting_par = False
    valid_pairs = 0
    for s in string:
        if s == '(' and starting_par == False:
            starting_par = True

        if s == ')' and starting_par == True:
            starting_par = False
            valid_pairs += 1

    return len(string) - valid_pairs * 2


if __name__ == "__main__":
    string = '()())())))()'
    print(remove_to_valid(string))
