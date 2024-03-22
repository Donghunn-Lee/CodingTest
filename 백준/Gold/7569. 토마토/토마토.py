# 토마토

import sys
from collections import deque
input = sys.stdin.readline

def bfs(tomatos):
    today = deque()
    visited = [[[False] * M for _ in range(N)] for _ in range(H)]
    unripe = 0
    date = 0

    for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomatos[i][j][k] == 1 and not visited[i][j][k]:
                    today.append((i, j, k))
                    visited[i][j][k] = True
                elif tomatos[i][j][k] == 0:
                    unripe += 1

    while True:
        next_day = deque()

        while today:
            ci, cj, ck = today.popleft()

            for ei,ej,ek in ((0, 1, 0), (0, 0, 1), (0, -1, 0), (0, 0, -1), (1, 0, 0), (-1, 0, 0)):
                ni, nj, nk = ci + ei, cj + ej, ck + ek
                if 0 <= ni < H and 0 <= nj < N and 0 <= nk < M and not visited[ni][nj][nk]:
                    if tomatos[ni][nj][nk] == 0:
                        tomatos[ni][nj][nk] = 1
                        unripe -= 1
                        next_day.append((ni, nj, nk))
                        visited[ni][nj][nk] = True
        
        if not next_day:
            if unripe:
                return -1
            else:
                return date

        date += 1
        today = next_day             


if __name__ == "__main__":
    M, N, H = map(int, input().split())
    tomatos = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
    print(bfs(tomatos))