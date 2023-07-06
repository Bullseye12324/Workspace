import sys
NO_PATH = float('inf')
# geeks example
input_1 = [[0, 5, NO_PATH, 10],
           [NO_PATH, 0, 3, NO_PATH],
           [NO_PATH, NO_PATH, 0,   1],
           [NO_PATH, NO_PATH, NO_PATH, 0]]

output_1 = [[0, 5, 8, 9],
            [NO_PATH, 0, 3, 4],
            [NO_PATH, NO_PATH, 0,   1],
            [NO_PATH, NO_PATH, NO_PATH, 0]]
# github negative edge example

input_2 = [[0, NO_PATH, 9, NO_PATH],
           [NO_PATH, 0, NO_PATH, NO_PATH],
           [NO_PATH, -5, 0, 8],
           [-3, 2, NO_PATH, 0]]

output_2 = [[0, 4, 9, 17],
            [NO_PATH, 0, NO_PATH, NO_PATH],
            [5, -5, 0, 8],
            [-3, 1, 6, 0]]

# 2 vertex graph example

input_3 = [[0, 2],
           [NO_PATH, 0]]

output_3 = [[0, 2],
            [NO_PATH, 0]]

# 2 vertex graph (no path) example

input_4 = [[0, NO_PATH],
           [NO_PATH, 0]]

output_4 = [[0, NO_PATH],
            [NO_PATH, 0]]

# 1 vertex graph example

input_5 = [[0]]

output_5 = [[0]]

# youtube example

input_6 = [[0, 3, NO_PATH, 7],
           [8, 0, 2, NO_PATH],
           [5, NO_PATH, 0, 1],
           [2, NO_PATH, NO_PATH, 0]]

output_6 = [[0, 3, 5, 6],
            [5, 0, 2, 3],
            [3, 6, 0, 1],
            [2, 5, 7, 0]]

# pre-brief example

input_7 = [[0, 7, NO_PATH, 8],
           [NO_PATH, 0, 5, NO_PATH],
           [NO_PATH, NO_PATH, 0, 2],
           [NO_PATH, NO_PATH, NO_PATH, 0]]

output_7 = [[0, 7, 12, 8],
            [NO_PATH, 0, 5, 7],
            [NO_PATH, NO_PATH, 0, 2],
            [NO_PATH, NO_PATH, NO_PATH, 0]]

# larger example for performance test

input_8 = [[0, 2, 2, NO_PATH, NO_PATH, NO_PATH],
           [NO_PATH, 0, 2, NO_PATH, NO_PATH, NO_PATH],
           [NO_PATH, NO_PATH, 0, 2, 2, 6],
           [NO_PATH, NO_PATH, NO_PATH, 0, NO_PATH, 2],
           [NO_PATH, NO_PATH, NO_PATH, NO_PATH, 0, 2],
           [NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, 0]]