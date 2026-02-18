# 17822 원판 돌리기

import sys
input = sys.stdin.readline


def spin(circle, d, k):
  k %= len(circle)
  if d == 0:
    circle[:] = circle[-k:] + circle[:-k]
  else:
    circle[:] = circle[k:] + circle[:k]


def remove_adjecent(circles, stack, N, M):
  global sum, count

  for i in range(N):
      for j in range(M):
          if j in stack[i]:
              sum -= circles[i][j]
              circles[i][j] = 0
              count -= 1


def adjust(circles, N, M):
  global sum, count
  if count == 0:
      return

  avg = sum / count

  for i in range(N):
      for j in range(M):
          if circles[i][j] == 0:
              continue
          if circles[i][j] > avg:
              circles[i][j] -= 1
              sum -= 1
          elif circles[i][j] < avg:
              circles[i][j] += 1
              sum += 1


def cal_circle(circles, N, M):
  stack = [set() for _ in range(N)]
  replaced = False

  for i in range(N):
    for j in range(M):
      if circles[i][j] == 0:
        continue

      nj = (j + 1) % M
      if circles[i][j] == circles[i][nj]:
        stack[i].add(j)
        stack[i].add(nj)
        replaced = True

      if i + 1 < N and circles[i][j] == circles[i + 1][j]:
        stack[i].add(j)
        stack[i + 1].add(j)
        replaced = True

  if replaced:
      remove_adjecent(circles, stack, N, M)
  else:
      adjust(circles, N, M)


def solve():
  N, M, T = map(int, input().split())
  circles = [list(map(int, input().split())) for _ in range(N)]
  cmd_list = [list(map(int, input().split())) for _ in range(T)]

  global sum, count
  sum = sum(map(sum, circles))
  count = N * M

  for x, d, k in cmd_list:
      for i in range(x, N + 1, x):
          spin(circles[i - 1], d, k)
      cal_circle(circles, N, M)

  print(sum)


if __name__ == '__main__':
  solve()
