def list_comprehension(x: int, y: int, z: int, n: int):
    return [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]


if __name__ == "__main__":
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    result = list_comprehension(x, y, z, n)
    print(result)
