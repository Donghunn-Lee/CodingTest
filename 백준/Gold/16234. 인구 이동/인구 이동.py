# 16234 인구 이동

from collections import deque
import sys
input = sys.stdin.readline

N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

visited = [[0]*N for _ in range(N)]
day = 0
answer = 0

while True:
    moved = False
    day += 1

    for i in range(N):
        for j in range(N):
            if visited[i][j] == day:
                continue

            cur = A[i][j]
            can_move = False
            for d in range(4):
                ni = i + dx[d]
                nj = j + dy[d]
                if 0 <= ni < N and 0 <= nj < N:
                    diff = cur - A[ni][nj]
                    if diff < 0:
                        diff = -diff
                    if L <= diff <= R:
                        can_move = True
                        break

            if not can_move:
                visited[i][j] = day
                continue

            q = deque([(i, j)])
            visited[i][j] = day
            union = [(i, j)]
            total = cur

            while q:
                x, y = q.popleft()
                cur = A[x][y]

                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]

                    if nx < 0 or nx >= N or ny < 0 or ny >= N:
                        continue
                    if visited[nx][ny] == day:
                        continue

                    diff = cur - A[nx][ny]
                    if diff < 0:
                        diff = -diff
                    if diff < L or diff > R:
                        continue

                    visited[nx][ny] = day
                    q.append((nx, ny))
                    union.append((nx, ny))
                    total += A[nx][ny]

            moved = True
            avg = total // len(union)
            for x, y in union:
                A[x][y] = avg

    if not moved:
        break

    answer += 1

print(answer)
