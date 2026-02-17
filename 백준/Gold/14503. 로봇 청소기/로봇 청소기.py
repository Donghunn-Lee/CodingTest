# 14503 로봇 청소기

import sys
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    robot = list(map(int, input().split()))
    room = [list(map(int, input().split())) for _ in range(N)]
    answer = 0

    # 북(0), 동(1), 남(2), 서(3)
    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    while True:
        ci, cj, cd = robot

        # 1. 현재 칸 청소
        if room[ci][cj] == 0:
            room[ci][cj] = -1
            answer += 1

        found = False

        # 2. 왼쪽 회전 4번
        for _ in range(4):
            cd = (cd + 3) % 4  # 왼쪽 회전
            di, dj = dir[cd]
            ni, nj = ci + di, cj + dj

            if room[ni][nj] == 0:
                robot = [ni, nj, cd]
                found = True
                break

        # 3. 네 방향 모두 실패 → 뒤로 이동
        if not found:
            di, dj = dir[(cd + 2) % 4]
            ni, nj = ci + di, cj + dj

            if room[ni][nj] != 1:
                robot = [ni, nj, cd]
            else:
                break

    print(answer)

if __name__ == '__main__':
    solve()
