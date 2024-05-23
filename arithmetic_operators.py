def arithmetic_operators(a: int, b: int):
    x, y, z = a + b, a - b, a * b
    print(x, y, z, sep="\n")


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    arithmetic_operators(a, b)