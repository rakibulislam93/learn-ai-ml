import numpy as np
x = np.array([5, 12, 25, 7, 30])

print(x[x > 15])  # Output: [20 30]



c = np.array([
    [10, 20, 3],
    [40, 50, 60]
])

print(c[c > 10])

result = np.where(c%2 == 0, 'Even', 'Odd')
print(result)