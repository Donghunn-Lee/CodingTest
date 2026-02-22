import sys
from collections import deque

input = sys.stdin.readline

def solve():
    R, C = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(R)]

    water_time = [[-1] * C for _ in range(R)]
    dist = [[-1] * C for _ in range(R)]

    wq = deque()
    sq = deque()

    for i in range(R):
        for j in range(C):
            if board[i][j] == '*':
                wq.append((i, j))
                water_time[i][j] = 0
            elif board[i][j] == 'S':
                sq.append((i, j))
                dist[i][j] = 0

    while wq:
        x, y = wq.popleft()
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C:
                if board[nx][ny] == '.' and water_time[nx][ny] == -1:
                    water_time[nx][ny] = water_time[x][y] + 1
                    wq.append((nx, ny))

    while sq:
        x, y = sq.popleft()
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C:
                if board[nx][ny] == 'D':
                    print(dist[x][y] + 1)
                    return
                if board[nx][ny] == '.' and dist[nx][ny] == -1:
                    nt = dist[x][y] + 1
                    if water_time[nx][ny] == -1 or nt < water_time[nx][ny]:
                        dist[nx][ny] = nt
                        sq.append((nx, ny))

    print("KAKTUS")

if __name__ == "__main__":
    solve()