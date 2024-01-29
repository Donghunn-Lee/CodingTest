from sys import stdin, stdout
input = stdin.readline
n = int(input())
for _ in range(n) :
    s = []
    a = input()
    for i in a :
        if i == '(' :
            s.append(i)
        elif i == ')' :
            if s :
                s.pop()
            else :
                print("NO")
                break
    else :
        print("YES") if not s else print("NO")