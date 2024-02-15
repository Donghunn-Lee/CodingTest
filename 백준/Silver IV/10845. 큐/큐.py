import sys

input = sys.stdin.readline
q = []

for _ in range(int(input())) :
    cmd = input().rstrip().split()
    if cmd[0] == "push" :
        q.append(cmd[1])
    elif cmd[0] == "pop" :
        print(q.pop(0) if q else -1)
    elif cmd[0] == "size":
        print(len(q))
    elif cmd[0] == "empty" :
        print(0 if q else 1)
    elif cmd[0] =="front" :
        print(q[0] if q else -1)
    elif cmd[0] == "back" :
        print(q[-1] if q else -1)