import numpy as np


def compute_cosine(x, y):
    return np.dot(x, y) / (np.linalg.norm(x)*np.linalg.norm(y))


x = np.array([1, 2, 3, 4])
y = np.array([1, 0, 3, 0])
result = compute_cosine(x, y)
print(round(result, 3))
