# 15683 감시

# js로는 예전에 풀었었고 어렴풋이 기억은 나는 문제
# 다만 파이썬으로 하려니 역시 기본문법이 퇴화해서 쉽지 않았음
# 생각없이 deepcopy 써서 풀다가, 백트래킹을 뒤늦게 생각했지만
# 방법이 헷갈려 지피티에게 문의

import sys
input = sys.stdin.readline

# 상, 우, 하, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# CCTV 타입별 가능한 방향 조합
cctv_dirs = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
}

def watch(x, y, d, changed):
    nx, ny = x, y
    while True:
        nx += dx[d]
        ny += dy[d]
        if nx < 0 or nx >= N or ny < 0 or ny >= M or board[nx][ny] == 6:
            break
        if board[nx][ny] == 0:
            board[nx][ny] = -1
            changed.append((nx, ny))

def dfs(idx):
    global answer

    if idx == len(cctvs):
        cnt = 0
        for i in range(N):
            cnt += board[i].count(0)
        answer = min(answer, cnt)
        return

    x, y, t = cctvs[idx]

    for dirs in cctv_dirs[t]:
        changed = []
        for d in dirs:
            watch(x, y, d, changed)

        dfs(idx + 1)

        # 원복
        for cx, cy in changed:
            board[cx][cy] = 0


# 입력
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

cctvs = []
for i in range(N):
    for j in range(M):
        if 1 <= board[i][j] <= 5:
            cctvs.append((i, j, board[i][j]))

answer = N * M
dfs(0)
print(answer)
