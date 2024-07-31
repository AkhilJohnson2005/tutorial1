import numpy as np

rows, columns = 6, 5
array_2d = np.fromfunction(lambda i, j: (i + j) % 2, (rows, columns), dtype=int)

print(array_2d)
