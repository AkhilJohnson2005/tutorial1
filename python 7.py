import numpy as np

def create_2d_array(value, rows):
    array_2d = np.tile(value, (rows, 1))
    return array_2d

# Example usage
value = [2, 2, 2, 2]
rows = 4
array_2d = create_2d_array(value, rows)

print("2D Array:")
print(array_2d)
