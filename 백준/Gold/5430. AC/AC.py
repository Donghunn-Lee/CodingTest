# AC

import sys
from collections import deque
input = sys.stdin.readline

def sol(cmd, lst):
    q = deque(lst)
    rev = False
    left, right = 0, 0

    cmd = cmd.replace('RR','')

    for c in cmd:
        if c == 'R':
            rev = not rev
        elif c == 'D':
            if rev:
                right += 1
            else:
                left += 1
    
    for _ in range(left):
        q.popleft()
    
    for _ in range(right):
        q.pop()
    
    if rev:
        q.reverse()

    return ''.join(str(list(q)).split())


if __name__ == "__main__":
    T = int(input())
    ans = []

    for _ in range(T):
        error = False
        cmd = input().rstrip()
        N = int(input())
        lst = eval(input().rstrip())

        if N < cmd.count('D'):
            ans.append('error')
        else:
            ans.append(sol(cmd, lst))
    
    print('\n'.join(ans))
