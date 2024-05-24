if __name__ == "__main__":
    n, m = [int(x) for x in input().split()]
    data = []
    for _ in range(n):
        data.append([int(x) for x in input().split()[:m]])
    k = int(input())
    data.sort(key=lambda x: x[k])
    for each in data:
        for num in each:
            print(num, end=" ")
        print()
