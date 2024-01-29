import sys
input = sys.stdin.readline
ls = list(input().rstrip())
rs = []
n = int(input())
for i in range(n):
    cmd = input().rstrip()
    if cmd == "L" and ls:
        rs.append(ls.pop())
    elif cmd == "D" and rs:
        ls.append(rs.pop())
    elif cmd == "B" and ls:
        ls.pop()
    elif "P" in cmd:
        ls.append(cmd[2])
ls.extend(rs[::-1])
print(''.join(ls))