# DSLR


import sys
from collections import deque
input = sys.stdin.readline

def bfs(a, b):
    q = deque()
    q.append(a)
    visited = [False] * 10000
    visited[a] = True
    cmd = ['' for _ in range(10000)]
    result = ''

    while q:
        cur = q.popleft()

        d = (cur * 2) % 10000
        s = cur - 1 if cur else 9999
        tmp = str(cur)
        tmp = '0' * (4 - len(tmp)) + tmp
        l = int(tmp[1:] + tmp[0])
        r = int(tmp[-1] + tmp[:-1])

        for i, j in ((d, 'D'), (s, 'S'), (l, 'L'), (r, 'R')):
             if not visited[i]:
                cmd[i] = cmd[cur] + j

                if i == b:                
                    result = cmd[i]
                    return result
                    # elif len(result) > len(cmd[i]):
                    #     result = cmd[i]
    
                q.append(i)
                visited[i] = True
    
    return result

if __name__ == "__main__":
    T = int(input())
    register = deque([0, 0, 0, 0, 0])
    ans = []

    for _ in range(T):
        A, B = map(int, input().split())
        ans.append(bfs(A, B))
    
    print('\n'.join(ans))