def sorting(s: str):
    odd, even = [], []
    small, caps = "", ""
    for i in s:
        if i.isalpha():
            if i.islower():
                small += i
            else:
                caps += i
        elif i.isdigit():
            even.append(int(i)) if int(i) % 2 == 0 else odd.append(int(i))
    return "".join(sorted(small) + sorted(caps) + list(map(str, sorted(odd))) + list(map(str, sorted(even))))


if __name__ == "__main__":
    s = "1qaz2wsx3edc4rfv5tgb6yhn7ujm8ik9ol0pQWERTYUIOPASDFGHJKLZXCVBNM"
    print(sorting(s))
    print(sorting(s) == "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468")
