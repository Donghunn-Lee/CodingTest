import sys, copy
input = sys.stdin.readline

def findCCTV():
    cctvs = []
    for i in range(N):
        for j in range(M):
            if 1 <= graph[i][j] <= 5:
                cctvs.append([i, j, graph[i][j]])
    return cctvs

def monitoring(board, si, sj, d):
    ni, nj = si, sj
    while True:
        ni += dy[d]
        nj += dx[d]

        if ni < 0 or ni >= N or nj < 0 or nj >= M:
            break
        if board[ni][nj] == 6:
            break
        if board[ni][nj] == 0:
            board[ni][nj] = -1

def countBlind(board):
    cnt = 0
    for i in range(N):
        cnt += board[i].count(0)
    return cnt

def dfs(cur_graph, cctvNum):
    global answer

    if cctvNum == len(cctvs):
        answer = min(answer, countBlind(cur_graph))
        return

    ci, cj, t = cctvs[cctvNum]

    # type 1,3,4 → 4방향 회전
    if t in [1, 3, 4]:
        for i in range(4):
            nxt_graph = copy.deepcopy(cur_graph)
            for d in cctv_types[t]:
                monitoring(nxt_graph, ci, cj, (d + i) % 4)
            dfs(nxt_graph, cctvNum + 1)

    # type 2 → 2방향
    elif t == 2:
        for i in range(2):
            nxt_graph = copy.deepcopy(cur_graph)
            for d in cctv_types[t]:
                monitoring(nxt_graph, ci, cj, (d + i) % 4)
            dfs(nxt_graph, cctvNum + 1)

    # type 5 → 고정
    else:
        nxt_graph = copy.deepcopy(cur_graph)
        for d in cctv_types[t]:
            monitoring(nxt_graph, ci, cj, d)
        dfs(nxt_graph, cctvNum + 1)


# main
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

cctv_types = [
    [],
    [0],          # 1
    [0, 2],       # 2
    [0, 1],       # 3
    [0, 1, 2],    # 4
    [0, 1, 2, 3]  # 5
]

cctvs = findCCTV()
answer = N * M

dfs(graph, 0)
print(answer)
