from sys import stdin, stdout
input = stdin.readline
n = int(input())
s = []
for _ in range(n) :
    cmd = input().rstrip()
    if cmd == 'pop' :
        stdout.write(s.pop()+"\n") if s else stdout.write("-1\n")
    elif cmd == 'size' :
        stdout.write(str(len(s))+"\n")
    elif cmd == 'empty':
        stdout.write("0\n" if s else "1\n")
    elif cmd == 'top' :
        stdout.write(s[-1]+"\n") if s else stdout.write("-1\n")
    else : s.append(cmd.split()[1])