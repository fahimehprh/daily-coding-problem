def get_next_cell(m, position, direction, visited_flag):
    x, y = position
    if direction == 'right':
        if y + 1 < len(m[0]) and not visited_flag[x][y + 1]:
            return (x, y + 1), 'right'
        elif x + 1 < len(m) and not visited_flag[x + 1][y]:
            return (x + 1, y), 'down'
    if direction == 'down':
        if x + 1 < len(m) and not visited_flag[x + 1][y]:
            return (x + 1, y), 'down'
        elif y - 1 >= 0 and not visited_flag[x][y - 1]:
            return (x, y - 1), 'left'
    if direction == 'left':
        if y - 1 >= 0 and not visited_flag[x][y - 1]:
            return (x, y - 1), 'left'
        elif x - 1 >= 0 and not visited_flag[x - 1][y]:
            return (x - 1, y), 'up'
    if direction == 'up':
        if x - 1 >= 0 and not visited_flag[x - 1][y]:
            return (x - 1, y), 'up'
        elif y + 1 < len(m[0]) and not visited_flag[x][y + 1]:
            return (x, y + 1), 'right'
    return None, None


def print_cell(m, position, direction, visited_flag, printed=[]):

    x, y = position
    visited_flag[x][y]  = True
    printed.append(m[x][y])
    (next_cell), new_direction = get_next_cell(m, position, direction, visited_flag)
    if next_cell:
        return print_cell(m, next_cell, new_direction, visited_flag, printed)
    return printed


def spiral(m):
    visited_flag = [[False for _ in range(len(m[0]))] for _ in range(len(m))]
    position = (0, 0)
    direction = 'right'
    return print_cell(m, position, direction, visited_flag)

        
if __name__ == "__main__":
    matrix = [[1,  2,  3,  4,  5],
                [6,  7,  8,  9,  10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20]]

    printed = spiral(matrix)
    for p in printed:
        print(p)
