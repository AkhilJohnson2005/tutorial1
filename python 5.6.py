import numpy as np

def create_2d_array(rows, columns, filler):
    array_2d = np.full((rows, columns), filler)
    return array_2d

def slice_2d_array(array, row_start, row_end, col_start, col_end):
    return array[row_start:row_end, col_start:col_end]

# Example usage
rows = 6
columns = 5
filler = 7
array_2d = create_2d_array(rows, columns, filler)

print("Original 2D Array:")
print(array_2d)

# Slicing the array using [-4:-1, -4:-1]
row_start, row_end = -4, -1
col_start, col_end = -4, -1
sliced_array = slice_2d_array(array_2d, row_start, row_end, col_start, col_end)

print("\nSliced 2D Array ([-4:-1, -4:-1]):")
print(sliced_array)
