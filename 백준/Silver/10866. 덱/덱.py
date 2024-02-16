# 덱(deque)

import sys
input = sys.stdin.readline

N = int(input())
deq = []
ans = []
def deque(cmd):

    if cmd[0] == 'push_front':
        deq.insert(0, cmd[1])
    elif cmd[0] == 'push_back':
        deq.append(cmd[1])
    elif cmd[0] == 'pop_front':
        if deq:
            ans.append(str(deq.pop(0)))
        else:
            ans.append('-1')
    elif cmd[0] == 'pop_back':
        if deq:
            ans.append(str(deq.pop()))
        else:
            ans.append('-1')
    elif cmd[0] == 'size':
        ans.append(str(len(deq)))
    elif cmd[0] == 'empty':
        if deq:
            ans.append('0')
        else:
            ans.append('1')
    elif cmd[0] == 'front':
        if deq:
            ans.append(str(deq[0]))
        else:
            ans.append('-1')
    elif cmd[0] == 'back':
        if deq:
            ans.append(str(deq[-1]))
        else:
            ans.append('-1')
    


for _ in range(N):
    cmd = input().split()
    deque(cmd)
print('\n'.join(ans))