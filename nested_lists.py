def second_lowest(data: list[list]):
    data.sort(key=lambda x: x[-1])
    second_lowest_students = []
    for i in range(1, len(data)):
        if data[i][-1] > data[0][-1]:
            second_lowest = data[i][-1]
            for j in range(i, len(data)):
                if data[j][-1] == second_lowest:
                    second_lowest_students.append(data[j][0])
                else:
                    break
            second_lowest_students.sort()
            for name in second_lowest_students:
                print(name)
            break


if __name__ == "__main__":
    data = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        data.append([name, score])
    second_lowest(data)
