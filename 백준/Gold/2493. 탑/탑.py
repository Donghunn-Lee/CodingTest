# 2493 탑

import sys
input = sys.stdin.readline



def solve():
  N = int(input())
  towers = list(map(int, input().split()))
  towers.reverse()
  result = [0] * N
  stack = []

  for i in range(N):
    if len(stack) == 0:
      stack.append([i, towers[i]])
      continue

    while len(stack) > 0 and stack[-1][1] <= towers[i]:
      idx = stack.pop()[0]
      result[idx] = N - i

    stack.append([i, towers[i]])

  result.reverse()

  print(' '.join(map(str, result)))




if __name__ == '__main__':
  solve()
