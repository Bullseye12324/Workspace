import itertools
import sys

NO_PATH = sys.maxsize

graph = [[0, 7, NO_PATH, 8],
         [NO_PATH, 0, 5, NO_PATH],
         [NO_PATH, NO_PATH, 0, 2],
         [NO_PATH, NO_PATH, NO_PATH, 0]]


def floydA(matrix):
    MAX_LENGTH = len(matrix[0])
    for start_node, end_node in itertools.product(range(MAX_LENGTH), range(MAX_LENGTH)):
        matrix[start_node][end_node] = shortestdistance(
            matrix, start_node, end_node, MAX_LENGTH)
    return matrix


def shortestdistance(matrix, start_node, end_node, intermediate):
    if intermediate < 0:
        return matrix[start_node][end_node]
    if start_node == end_node:
        return matrix[start_node][end_node]
    starttoend = shortestdistance(matrix, start_node, end_node, intermediate-1)
    starttointer = shortestdistance(
        matrix, start_node, intermediate-1, intermediate-1)
    intertoend = shortestdistance(
        matrix, intermediate-1, end_node, intermediate-1)
    min_value = min(starttoend, starttointer+intertoend)
    return min_value


output = floydA(graph)
print(output)
