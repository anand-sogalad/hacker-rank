def any_or_all():
    n = int(input())
    data = list(map(int, input().split()[:n]))
    return any([str(j) == str(j)[::-1] for j in data if all([i > 0 for i in data])])


if __name__ == "__main__":
    print(any_or_all())
