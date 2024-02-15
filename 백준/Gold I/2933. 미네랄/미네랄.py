# 미네랄

import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
cave = [list(input().rstrip()) for _ in range(R)]
N = int(input())
stick_height = list(map(int, input().split()))
directions = ((-1, 0), (1, 0), (0, 1), (0, -1))

def throwing_stick(h, n) :
    if n % 2:
        for i in range(1, C + 1):
            if cave[h][C - i] == 'x':
                cave[h][C - i] = '.'
                return (h, C - i)
    else:
        for i in range(C):
            if cave[h][i] == 'x':
                cave[h][i] = '.'
                return (h, i)

def check_cluster(p):
    v_cave = [[False] * C for _ in range(R)]
    q = deque()
    visited = []
    cluster, ground = [], []

    for c in directions:
        ni, nj = p[0] + c[0], p[1] + c[1]
        if 0 <= ni < R and 0 <= nj < C:
            if cave[ni][nj] == 'x':
                cluster.append((ni, nj))

    for cl_num in range(1, len(cluster)+1):
        q.append(cluster[cl_num - 1])
        visited.append(cluster[cl_num - 1])
        if cl_num not in ground:
            while q:
                cx, cy = q.popleft()
                for c in directions:
                    ni, nj = cx + c[0], cy + c[1]
                    if 0 <= ni < R and 0 <= nj < C:
                        if cave[ni][nj] == 'x':
                            if ni == R - 1 or v_cave[ni][nj] in ground:
                                ground.append(cl_num)
                                q = deque()
                                visited = []
                                break
                            elif v_cave[ni][nj] == False :
                                q.append((ni, nj))
                                visited.append([ni, nj])
                                v_cave[ni][nj] = cl_num
            if visited:
                return visited

def fall_down(v):
    fallen = []
    n = 1
    while True:
        for i in v:
            row = i[0] + n
            if [row, i[1]] not in v:
                if 0 <= row <= R:
                    if row == R or cave[row][i[1]] == 'x':
                        for j in v:
                            fallen.append([j[0] + (n - 1), j[1]])
                        for j in v:
                            if j not in fallen:
                                cave[j[0]][j[1]] = '.'
                        for j in fallen:
                            cave[j[0]][j[1]] = 'x'
                        return
        n += 1

for i in range(N):
    hit_point = throwing_stick(R-stick_height[i], i)

    if hit_point :
        breaked = check_cluster(hit_point)
        if breaked:
            fall_down(breaked)

for i in range(R):
    for j in range(C):
        print(cave[i][j], end='')
    print()