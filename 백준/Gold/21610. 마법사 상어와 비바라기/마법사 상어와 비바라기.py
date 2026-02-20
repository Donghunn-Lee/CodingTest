import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

moves = []
for _ in range(M):
    d, s = map(int, input().split())
    moves.append((d - 1, s))

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

diag = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

# 초기 구름
clouds = [(N-1,0),(N-1,1),(N-2,0),(N-2,1)]

for d, s in moves:
    cloud_map = [[False]*N for _ in range(N)]
    new_clouds = []

    # 구름 이동 + 비
    for x, y in clouds:
        nx = (x + dx[d]*s) % N
        ny = (y + dy[d]*s) % N
        A[nx][ny] += 1
        cloud_map[nx][ny] = True
        new_clouds.append((nx, ny))

    # 물복사
    for x, y in new_clouds:
        cnt = 0
        for ddx, ddy in diag:
            nx, ny = x + ddx, y + ddy
            if 0 <= nx < N and 0 <= ny < N and A[nx][ny] > 0:
                cnt += 1
        A[x][y] += cnt

    # 새 구름 생성
    clouds = []
    for i in range(N):
        for j in range(N):
            if not cloud_map[i][j] and A[i][j] >= 2:
                A[i][j] -= 2
                clouds.append((i, j))

print(sum(map(sum, A)))