import numpy as np

x = np.array([0.19, 0.24, 0.8, 0.25, 0.03, 0.017])
y = np.array([1, 0, 0, 1, 1, 1])
print(np.corrcoef(x, y))
print(np.corrcoef(x, y)[1][0])