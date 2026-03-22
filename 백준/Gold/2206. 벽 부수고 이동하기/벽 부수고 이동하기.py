from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append((0, 0, 0))  # x, y, broke

    visited = [[[0] * M for _ in range(N)] for _ in range(2)]
    visited[0][0][0] = 1

    while q:
        x, y, broke = q.popleft()

        if x == N - 1 and y == M - 1:
            return visited[broke][x][y]

        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy

            if not (0 <= nx < N and 0 <= ny < M):
                continue

            if graph[nx][ny] == '0' and not visited[broke][nx][ny]:
                visited[broke][nx][ny] = visited[broke][x][y] + 1
                q.append((nx, ny, broke))

            elif graph[nx][ny] == '1' and broke == 0 and not visited[1][nx][ny]:
                visited[1][nx][ny] = visited[0][x][y] + 1
                q.append((nx, ny, 1))

    return -1


N, M = map(int, input().split())
graph = [input().rstrip() for _ in range(N)]

print(bfs())