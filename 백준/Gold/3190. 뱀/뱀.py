from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
K = int(input())

# 보드: 0 빈칸, 1 사과
board = [[0] * N for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    board[r - 1][c - 1] = 1

L = int(input())
turns = {}
for _ in range(L):
    t, d = input().split()
    turns[int(t)] = d

# 방향: 오른쪽, 아래, 왼쪽, 위 (시계방향)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
direction = 0  # 처음엔 오른쪽

snake = deque()
snake.append((0, 0))
snake_set = {(0, 0)}  # 몸 충돌 체크용

time = 0
x, y = 0, 0

while True:
    time += 1
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 벽 충돌
    if not (0 <= nx < N and 0 <= ny < N):
        break

    # 자기 몸 충돌
    if (nx, ny) in snake_set:
        break

    # 머리 이동
    snake.append((nx, ny))
    snake_set.add((nx, ny))

    # 사과 있으면 꼬리 유지
    if board[nx][ny] == 1:
        board[nx][ny] = 0
    else:
        tx, ty = snake.popleft()
        snake_set.remove((tx, ty))

    # 방향 전환
    if time in turns:
        if turns[time] == 'L':
            direction = (direction - 1) % 4
        else:  # 'D'
            direction = (direction + 1) % 4

    x, y = nx, ny

print(time)