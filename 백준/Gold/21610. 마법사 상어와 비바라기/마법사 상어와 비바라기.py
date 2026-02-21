# 21610 마법사 상어와 비바라기

import sys
input = sys.stdin.readline

def solve():
  N, M = map(int, input().split())
  board = [list(map(int, input().split())) for _ in range(N)]
  cmds = [list(map(int, input().split())) for _ in range(M)]
  dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
  dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]
  cross_dir = [2, 4, 6, 8]
  
  cloud = [[N - 1, 0], [N - 1, 1], [N - 2, 0], [N - 2, 1]]
  for d, s in cmds:
    increased = [[False] * N for _ in range(N)]
  
    for i in range(len(cloud)):
      ni = (cloud[i][0] + dy[d] * s) % N
      nj = (cloud[i][1] + dx[d] * s) % N
      cloud[i] = [ni, nj]
      board[ni][nj] += 1
      increased[ni][nj] = True

    for i, j in cloud:
      cross_water = 0

      for cd in cross_dir:
        nci = i + dy[cd]
        ncj = j + dx[cd]

        if 0 <= nci < N and 0 <= ncj < N and board[nci][ncj] > 0:
          cross_water += 1
      
      board[i][j] += cross_water
    
    cloud = []

    for i in range(N):
      for j in range(N):
        if board[i][j] >= 2 and not increased[i][j]:
          board[i][j] -= 2
          cloud.append([i, j])

  print(sum(map(sum, board)))

if __name__ == '__main__':
  solve()