# 14499 주사위 굴리기

import sys
input = sys.stdin.readline

def move(dice, dir, bottom):
  if dir == 1:
    tmp = dice[0][2]
    dice[0] = [bottom] + dice[0][:2]
    dice[1][1] = dice[0][1]
    bottom = tmp
  elif dir == 2:
    tmp = dice[0][0]
    dice[0] = dice[0][1:] + [bottom]
    dice[1][1] = dice[0][1]
    bottom = tmp
  elif dir == 3:
    tmp = dice[1][0]
    dice[1] = dice[1][1:] + [bottom]
    dice[0][1] = dice[1][1]
    bottom = tmp
  else:
    tmp = dice[1][2]
    dice[1] = [bottom] + dice[1][:2]
    dice[0][1] = dice[1][1]
    bottom = tmp
  
  return bottom


def solve():
  N, M, x, y, K = map(int, input().split())
  board = [list(map(int, input().split())) for _ in range(N)]
  cmds = list(map(int, input().split()))
  dx = [0, 1, -1, 0, 0]
  dy = [0, 0, 0, -1, 1]
  ci, cj = x, y

  # 가로 + 세로 + 밑면으로 주사위 관리
  # [[4, 1, 3] 가로
  # ,[2, 1, 5]] 세로
  # 6 밑면
  dice = [[0] * 3 for _ in range(2)]
  bottom = 0

  result = []

  for cmd in cmds:
    ni, nj = ci + dy[cmd], cj + dx[cmd]

    if 0 <= ni < N and 0 <= nj < M:
      bottom = move(dice, cmd, bottom)

      if board[ni][nj] == 0:
        board[ni][nj] = bottom
      else :
        bottom = board[ni][nj]
        board[ni][nj] = 0
      
      result.append(dice[0][1])
      ci, cj = ni, nj



  print('\n'.join(map(str, result)))

if __name__ == '__main__':
  solve()