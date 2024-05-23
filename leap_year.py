def is_leap(n: int):
    if n % 4 == 0:
        if n % 100 != 0 or n % 400 == 0:
            return True
        return False
    return False


if __name__ == "__main__":
    year = int(input())
    print(is_leap(year))