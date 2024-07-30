import numpy as np


def compute_eigenvalues_eigenvectors(matrix):

    eigenvalues, eigenvectors = np.linalg.eig(matrix)

    eigenvectors = eigenvectors / np.linalg.norm(eigenvectors, axis=0)
    return eigenvalues, eigenvectors


if __name__ == "__main__":
    A = np.array([[0.9, 0.2], [0.1, 0.8]])

    eigenvalues, eigenvectors = compute_eigenvalues_eigenvectors(A)

    print(eigenvalues)
    print(eigenvectors)
