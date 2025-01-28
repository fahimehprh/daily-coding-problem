"""
Given an undirected graph represented as an adjacency matrix and an integer k, 
write a function to determine whether each vertex in the graph can be colored 
such that no two adjacent vertices share the same color using at most k colors.
"""


def color_graph(matrix, current_node, colors, nodes_color):
    neigbors_colors = []
    uncolored_neigbors = []
    for i in range(len(matrix)):
        if matrix[current_node][i] == 1:
            if i in nodes_color.keys():
                neigbors_colors.append(nodes_color[i])
            else:
                uncolored_neigbors.append(i)
    
    node_color = min([color for color in colors if color not in neigbors_colors])
    nodes_color[current_node] = node_color

    for n in uncolored_neigbors:
        color_graph(matrix, n, colors, nodes_color)


def get_min_color(matrix):
    nodes_count = len(matrix)
    colors = range(nodes_count)
    nodes_color = {}
    for i in range(nodes_count):
        if i not in nodes_color.keys():
            color_graph(matrix, i, colors, nodes_color)
    
    return(max(nodes_color.values()) + 1)
    

def can_color(matrix, k):
    min_color = get_min_color(matrix)
    if min_color <= k:
        return True
    return False


if __name__ == "__main__":
    adjacency_matrix = [
        [0, 1, 1, 1],
        [1, 0, 1, 1],
        [1, 1, 0, 1],
        [1, 1, 1, 0],
    ]

    # adjacency_matrix = [
    #     [0, 1, 0, 0],
    #     [1, 0, 1, 0],
    #     [0, 1, 0, 1],
    #     [0, 0, 1, 0],
    # ]

    print(can_color(adjacency_matrix, 4))
    print(can_color(adjacency_matrix, 3))
