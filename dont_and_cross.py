import numpy as np


def matrix_multiplication(m1, m2):
    # np.dot used to find matrix multiplication
    return np.dot(m1, m2)


if __name__ == "__main__":
    n = int(input())
    m1 = np.array([[int(x) for x in input().split()] for _ in range(n)])
    m2 = np.array([[int(x) for x in input().split()] for _ in range(n)])
    x = matrix_multiplication(m1, m2)
    print(x)
