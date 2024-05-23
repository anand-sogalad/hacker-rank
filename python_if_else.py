def if_else(n: int):
    if n % 2 != 0:
        return "Weird"
    if 2 <= n <= 5:
        return "Not Weird"
    if 6 <= n <= 20:
        return "Weird"
    return "Not Weird"


if __name__ == "__main__":
    n = int(input().strip())
    x = if_else(n)
    print(x)
