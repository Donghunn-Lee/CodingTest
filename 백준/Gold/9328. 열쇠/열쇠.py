# 열쇠

import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    global count

    deq = deque()
    deq.append((0, 0))
    visited = [[0] * (W + 2) for _ in range(H + 2)]
    visited[0][0] = 1

    while deq:
        ci, cj = deq.popleft()

        for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            ni, nj = ci + di, cj + dj

            if 0 <= ni < H + 2 and 0 <= nj < W + 2 and not visited[ni][nj] and building[ni][nj] != '*':
                nxt = building[ni][nj]

                if nxt == '.':
                    deq.append((ni, nj))
                
                elif nxt == '$':
                    count += 1
                    deq.append((ni, nj))
                
                elif 65 <= ord(nxt) <= 90:
                    if chr(ord(nxt) + 32) in visited_keys:
                        deq.append((ni, nj))

                    else:
                        if visited_door.get(nxt):
                            visited_door[nxt].append((ni, nj))
                        else:
                            visited_door[nxt] = [(ni, nj)]

                elif 97 <= ord(nxt) <= 122:
                    visited_keys.add(nxt)
                    deq.append((ni, nj))
                    
                    if visited_door.get(chr(ord(nxt) - 32)):
                        for t_ni, t_nj in visited_door[chr(ord(nxt) - 32)]:                        
                            deq.append((t_ni, t_nj))
                    
                visited[ni][nj] = 1


if __name__ == "__main__":
    T = int(input())
    ans = []

    for _ in range(T):
        H, W = map(int, input().split())
        building = ['.' + input().rstrip() + '.' for _ in range(H)]
        building = ['.' * (W + 2)] + building + ['.' * (W + 2)]
        visited_door, visited_keys = dict(), set()
        keys = list(input().rstrip())
        for k in keys:
            visited_keys.add(k)

        count = 0
        bfs()

        ans.append(str(count))
    
    print("\n".join(ans))