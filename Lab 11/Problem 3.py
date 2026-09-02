import numpy as np

mat = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

column_sum = np.sum(mat, axis=0)
row_sum = np.sum(mat, axis=1)

print("Column sums:")
print(column_sum)

print("Row sums:")
print(row_sum)