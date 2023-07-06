import testexamples as t
import itertools

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


def floydAIterative(matrix):
    V = len(matrix[0])
    dist = list(map(lambda i: list(map(lambda j: j, i)), matrix))
    for k in range(V):

        # pick all vertices as source one by one
        for i in range(V):

            # Pick all vertices as destination for the
            # above picked source
            for j in range(V):

                # If vertex k is on the shortest path from
                # i to j, then update the value of dist[i][j]
                dist[i][j] = min(dist[i][j],
                                 dist[i][k] + dist[k][j]
                                 )
    return dist


interativeoutput = floydAIterative(t.input_7)
recursiveoutput = floydA(t.input_7)
