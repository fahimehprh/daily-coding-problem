def get_subsets(cur_set):
    l = len(cur_set)
    if l == 0:
        return [[]]
    cur_item = cur_set[-1]
    sub = get_subsets(cur_set[:l-1])
    new_sub = sub[:]
    for s in sub:
        new_sub.append(s + [cur_item])
    return new_sub

if __name__ == "__main__":
    numbers = [int(x) for x in input().strip().split()]
    print(get_subsets(numbers))
