import numpy as np

arr = np.array([10, -5, 20, -10, 30, -2])

arr[arr < 0] = 0

print("Array after replacing negative values:")
print(arr)