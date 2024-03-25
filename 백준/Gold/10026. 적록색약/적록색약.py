# 적록색약

# 2트 끝에 포기하고 모범 답안을 검색함. 내가 졌다.
# 1트는 dfs를 돌리다가 R에서 G, 또는 반대 경우를 발견하면 그 좌표를 기준으로 다른 dfs를 돌리는 방법.
# 2트는 R과 B 먼저 찾고 돌릴 때 각 구역별 고유 flag를 부여, G를 찾을 때 flag로 중복을 고려해 인접 개수를 세는 방법.
# 두 방법 다 틀려서 도대체 어떻게 해야하지, dfs로 flag부여까지 한 다음에 그걸로 연결리스트를 만들어야 하나까지 생각.
# 끝내 포기하고 찾아보니 그냥 R과 G를 합치고 한 번 더 탐색하면 되는 문제였음.. 오기부리지 말걸 3시간 좀 더 날린 듯.

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

# 입력 색을 기준으로 구역을 찾는 함수.
def dfs(visited, color, ci, cj):
    visited[ci][cj] = True

    for d in dir:
        ni, nj = ci + d[0], cj + d[1]
        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
            if grid[ni][nj] == color:
                dfs(visited, color, ni, nj)

# R을 G로 변환해서 적록색약인 시점을 만드는 함수.
def convert_R_to_G():
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 'R':
                grid[i][j] = 'G'


if __name__ == "__main__":
    N = int(input())
    grid = [list(input().rstrip()) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    dir = ((1, 0), (0, 1), (-1, 0), (0, -1))
    count = 0       # 일반인 시점 구역 수.
    count_RG = 0    # 적록색약인 시점 구역 수

    # 우선 병합 전 일반인이 보는 구역 수를 검사.
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                dfs(visited, grid[i][j], i, j)
                count += 1

    # R과 G 병합.
    convert_R_to_G()

    visited_ = [[False] * N for _ in range(N)]

    # R과 G가 병합된 적록색약인이 보는 구역 수를 검사.
    for i in range(N):
        for j in range(N):
            if not visited_[i][j]:
                dfs(visited_, grid[i][j], i, j)
                count_RG += 1

    print(count, count_RG)
