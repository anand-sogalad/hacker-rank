def python_division(a: int, b: int):
    x, y = a // b, a / b
    print(x, y, sep="\n")


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    python_division(a, b)
