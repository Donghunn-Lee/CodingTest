# 경사로

import sys
input = sys.stdin.readline  

def can_pass(line):
  used = [False] * N
  
  for i in range(N - 1):
    cur = line[i]
    nxt = line[i + 1]

    # 높이 동일 -> 전진 가능
    if cur == nxt:
      continue

    # 높이차 2 이상 -> 전진 불가
    if abs(cur - nxt) > 1:
      return False
    
    # 높이차 1 -> 경사로 설치 시도
    if cur + 1 == nxt:
      for j in range(i, i - L, -1):
        if j < 0 or line[j] != cur or used[j]:
          return False
        used[j] = True

    elif cur -1 == nxt:
      for j in range(i + 1, i + 1 + L):
        if j >= N or line[j] != nxt or used[j]:
          return False
        used[j] = True
  
  return True

if __name__ == '__main__' :
  N, L = map(int, input().split())
  board = [list(map(int, input().split())) for _ in range(N)]
  answer = 0

  for i in range(N):
    if can_pass(board[i]):
      answer += 1
  
  for j in range(N):
    col = [board[i][j] for i in range(N)]
    if can_pass(col):
      answer += 1

  print(answer)



