import numpy as np

def create_2d_array(rows, columns, filler):
    array_2d = np.full((rows, columns), filler)
    return array_2d

def find_dimensions(array):
    return array.shape

# Example usage
rows = 6
columns = 5
filler = 7
array_2d = create_2d_array(rows, columns, filler)

print("Original 2D Array:")
print(array_2d)

dimensions = find_dimensions(array_2d)
print("\nDimensions of the array:", dimensions)
