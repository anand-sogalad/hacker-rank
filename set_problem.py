n = int(input())
s = set(list(map(int, input().split()[:n])))
commands = {
    "pop": s.pop,
    "remove": s.remove,
    "discard": s.discard,
}
for _ in range(int(input())):
    command = input().split()
    if len(command) > 1:
        commands[command[0]](int(command[1]))
    else:
        commands[command[0]]()

print(sum(s))
