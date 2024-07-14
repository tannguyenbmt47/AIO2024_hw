import numpy as np

# Độ dài của vector


def compute_vector_length(vector):

    len_of_vector = np.linalg.norm(vector)

    return len_of_vector


def compute_dot_product(vector1, vector2):
    result = np.dot(vector1, vector2)

    return result


def matrix_multi_vector(matrix, vector):
    result = matrix @ vector

    return result


def matrix_multi_matrix(matrix1, matrix2):
    result = matrix1 @ matrix2

    return result


def inverse_matrix(matrix):
    det = np.linalg.det(matrix)
    if det == 0:
        raise ValueError("Matrix is not invertible")

    result = np.linalg.inv(matrix)
    return result


if __name__ == "__main__":

    # bài 1
    vector = np.array([-2, 4, 9, 21])
    result = compute_vector_length([vector])
    print(round(result, 2))

    # bài 2
    v1 = np.array([0, 1, -1, 2])
    v2 = np.array([2, 5, 1, 0])
    result = compute_dot_product(v1, v2)
    print(round(result, 2))

    # bài 3
    x = np.array([[1, 2],
                  [3, 4]])
    k = np.array([1, 2])
    print('result \n', x.dot(k))
    print(compute_dot_product(x, k))

    # bài 4
    x = np.array([[-1, 2],
                  [3, -4]])
    k = np.array([1, 2])
    print('result \n', x@k)

    # bài 5
    m = np.array([[-1, 1, 1], [0, -4, 9]])
    v = np.array([0, 2, 1])
    result = matrix_multi_vector(m, v)
    print(result)

    # bài 6
    m1 = np.array([[0, 1, 2], [2, -3, 1]])
    m2 = np.array([[1, -3], [6, 1], [0, -1]])
    result = matrix_multi_matrix(m1, m2)
    print(result)

    # BÀI 7
    m1 = np.eye(3)
    m2 = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
    result = m1@m2
    print(result)

    # BÀI 8
    m1 = np.eye(2)
    m1 = np.reshape(m1, (-1, 4))[0]
    m2 = np.array([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]])
    result = m1@m2
    print(result)

    # Bài 9
    m1 = np.array([[1, 2], [3, 4]])
    m1 = np.reshape(m1, (-1, 4), "F")[0]
    m2 = np.array([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]])
    result = m1@m2
    print(result)

    # bài 10
    m1 = np.array([[-2, 6], [8, -4]])
    result = inverse_matrix(m1)
    print(result)

# 1d, 2b, 3a , 4b , 5a, 6c, 7a, 8d, 9b, 10a
