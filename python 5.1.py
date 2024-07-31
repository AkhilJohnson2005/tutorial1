import numpy as np

def create_2d_array(rows, columns, filler):
    array_2d = np.full((rows, columns), filler)
    return array_2d

def slice_2d_array(array, row_slice=slice(None), col_slice=slice(None)):
    return array[row_slice, col_slice]

# Example usage
rows = 6
columns = 5
filler = 7
array_2d = create_2d_array(rows, columns, filler)

print("Original 2D Array:")
print(array_2d)

# Slicing the array using [:, :]
sliced_array = slice_2d_array(array_2d, row_slice=slice(None), col_slice=slice(None))

print("\nSliced 2D Array ([:, :]):")
print(sliced_array)
