import numpy as np


def snail(array):
    array_np = np.array(array)
    result = []
    aux = []
    for i in range(len(array) * 2 - 1):
        aux.append(array_np[0])
        array_np = np.flipud(array_np[1:].transpose())
    for row in aux:
        for cell in row:
            result.append(cell)
    return result


array_1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
expected_1 = [1, 2, 3, 6, 9, 8, 7, 4, 5]
assert snail(array_1) == expected_1

array_2 = [[1, 2, 3],
           [8, 9, 4],
           [7, 6, 5]]
expected_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert snail(array_2) == expected_2
