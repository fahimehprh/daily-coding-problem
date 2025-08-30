def dfs(m, i, j, visited):
    neighbors = [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]
    visited[i][j] = True
    for n_i, n_j in neighbors:
        if n_i >= 0 and n_i < len(m) and n_j >=0 and n_j < len(m[0]) and m[n_i][n_j] == 1 and visited[n_i][n_j] == False:
            dfs(m, n_i, n_j, visited)


def number_of_islands(matrix):
    visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    islands = 0

    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            if matrix[i][j] == 1 and visited[i][j] == False:
                dfs(matrix, i, j, visited)
                islands += 1

    return islands


if __name__ == "__main__":
    matrix = [
        [1, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 1, 0, 0, 1]
    ]

    print(number_of_islands(matrix))