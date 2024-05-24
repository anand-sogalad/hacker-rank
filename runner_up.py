def runner_up(data: list):
    data.sort(reverse=True)
    max_score = data[0]
    for score in data:
        if score < max_score:
            return score


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    result = runner_up(arr)
    print(result)
