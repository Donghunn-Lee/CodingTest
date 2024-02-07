# 백조의 호수

import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
lake = [list(input().strip()) for _ in range(R)]
date = 0
w_map = [[False] * C for _ in range(R)]
s_map = [[False] * C for _ in range(R)]
swan, swan_n = deque(), deque()
L1, L2 = (), ()
water, melting = deque(), deque()
directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]

def update () :
    while water:
        ci, cj = water.popleft()
        lake[ci][cj] = '.'
        for d in directions:
            ni, nj = ci + d[0], cj + d[1]
            if 0 <= ni < R and 0 <= nj < C and (ni, nj) and w_map[ni][nj] == False:
                if lake[ni][nj] == '.':
                    water.append((ni, nj))
                else:
                    melting.append((ni, nj))
                w_map[ni][nj] = True

def swimming () :
    while swan:
        ci, cj = swan.popleft()
        
        if (ci, cj) == L2:
            return True

        for d in directions:
            ni, nj = ci + d[0], cj + d[1]
            if 0 <= ni < R and 0 <= nj < C and (ni, nj) and s_map[ni][nj] == False:
                if lake[ni][nj] == '.':
                    swan.append((ni, nj))
                else :
                    swan_n.append((ni, nj))
                s_map[ni][nj] = True
    return False

for i in range(R):
    for j in range(C):
        if lake[i][j] == 'L':
            if swan:
                L2 = (i,j)      # 찾을 타겟이 되는 백조 L2
            else:
                swan.append((i,j))
                s_map[i][j] = True # 탐색 시작점이 되는 백조 L1
            lake[i][j] = '.'
        if lake[i][j] == '.':
            water.append((i,j))
            w_map[i][j] = True

while True:
    update()

    if swimming():
        print(date)
        break
    
    swan = swan_n
    water = melting
    swan_n, melting = deque(), deque()
    date += 1




                
                    
        



# # 1) .을 따라갔을 때 다른 L을 만나는지 판별하는 알고리즘
# # 2) x를 .로 바꾸는 알고리즘