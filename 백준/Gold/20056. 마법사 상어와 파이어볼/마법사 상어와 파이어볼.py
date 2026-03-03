# 20056 마법사 상어와 파이어볼

from collections import defaultdict

import sys
input = sys.stdin.readline

dr = [-1,-1,0,1,1,1,0,-1]
dc = [0,1,1,1,0,-1,-1,-1]

def move_fireballs(fireballs, N):
    board = defaultdict(list)

    for r, c, m, s, d in fireballs:
        nr = (r + dr[d] * s) % N
        nc = (c + dc[d] * s) % N
        board[(nr, nc)].append((m, s, d))

    return board


def split_fireballs(board):
    new_fireballs = []

    for (r, c), balls in board.items():

        if len(balls) == 1:
            m, s, d = balls[0]
            new_fireballs.append((r, c, m, s, d))
            continue

        total_m = sum(b[0] for b in balls)
        total_s = sum(b[1] for b in balls)

        count = len(balls)

        new_m = total_m // 5
        if new_m == 0:
            continue

        new_s = total_s // count

        all_even = all(b[2] % 2 == 0 for b in balls)
        all_odd = all(b[2] % 2 == 1 for b in balls)

        if all_even or all_odd:
            dirs = [0,2,4,6]
        else:
            dirs = [1,3,5,7]

        for d in dirs:
            new_fireballs.append((r, c, new_m, new_s, d))

    return new_fireballs


def solve():
    N, M, K = map(int, input().split())
    fireballs = []

    for _ in range(M):
        r, c, m, s, d = map(int, input().split())
        fireballs.append((r-1, c-1, m, s, d))

    for _ in range(K):
        board = move_fireballs(fireballs, N)
        fireballs = split_fireballs(board)

    print(sum(f[2] for f in fireballs))


solve()