# 집합

import sys
input = sys.stdin.readline

def add(n):
    S.add(n)

def remove(n):
    S.discard(n)

def check(n):
    if n in S:
        print(1)
    else:
        print(0)

def toggle(n):
    if n in S:
        S.remove(n)
    else:
        S.add(n)

def all():
    global S
    S = set(range(1, 21))

def empty():
    global S
    S = set()

if __name__ == "__main__":
    M = int(input())
    S = set()

    for _ in range(M):
        cmd = input().rstrip().split()

        if cmd[0] == 'add':
            add(int(cmd[1]))
        
        elif cmd[0] == 'remove':
            remove(int(cmd[1]))
        
        elif cmd[0] == 'check':
            check(int(cmd[1]))
        
        elif cmd[0] == 'toggle':
            toggle(int(cmd[1]))
        
        elif cmd[0] == 'all':
            all()
        
        elif cmd[0] == 'empty':
            empty()
