if __name__ == "__main__":
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *scores = input().split()
        scores = list(map(float, scores))
        student_marks[name] = scores
    query_name = input()
    x = student_marks.get(query_name)
    print(f"{sum(x) / len(x):.2f}")
