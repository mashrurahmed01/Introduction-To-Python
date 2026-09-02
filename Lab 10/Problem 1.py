import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

new_shape = arr.reshape(2, 3)

print("Original array:")
print(arr)

print("Reshaped array:")
print(new_shape)