import numpy as np

arr = np.array([10, 20, 30, 20, 40, 20, 50])

item = 20
n = 2

positions = np.where(arr == item)[0]

if len(positions) >= n:
    print("Index of the", n, "occurrence of", item, "is:", positions[n - 1])
else:
    print("The item does not occur", n, "times.")