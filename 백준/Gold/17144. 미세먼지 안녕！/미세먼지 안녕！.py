import sys
input = sys.stdin.readline


def spread_dust(board, R, C):
    """미세먼지 확산"""
    nxt = [[0] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if board[i][j] > 0:
                amount = board[i][j] // 5
                spread_cnt = 0

                for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < R and 0 <= nj < C and board[ni][nj] != -1:
                        nxt[ni][nj] += amount
                        spread_cnt += 1

                nxt[i][j] += board[i][j] - amount * spread_cnt

    # 공기청정기 위치 유지
    for i in range(R):
        if board[i][0] == -1:
            nxt[i][0] = -1
            nxt[i + 1][0] = -1
            break

    return nxt


def clean_air(board, upper, lower, R, C):
    """공기청정기 순환"""

    # 위쪽 (반시계)
    for i in range(upper - 1, 0, -1):
        board[i][0] = board[i - 1][0]
    for j in range(C - 1):
        board[0][j] = board[0][j + 1]
    for i in range(upper):
        board[i][C - 1] = board[i + 1][C - 1]
    for j in range(C - 1, 1, -1):
        board[upper][j] = board[upper][j - 1]
    board[upper][1] = 0

    # 아래쪽 (시계)
    for i in range(lower + 1, R - 1):
        board[i][0] = board[i + 1][0]
    for j in range(C - 1):
        board[R - 1][j] = board[R - 1][j + 1]
    for i in range(R - 1, lower, -1):
        board[i][C - 1] = board[i - 1][C - 1]
    for j in range(C - 1, 1, -1):
        board[lower][j] = board[lower][j - 1]
    board[lower][1] = 0


def solve():
    R, C, T = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(R)]

    # 공기청정기 위치 찾기
    for i in range(R):
        if board[i][0] == -1:
            upper = i
            lower = i + 1
            break

    for _ in range(T):
        board = spread_dust(board, R, C)
        clean_air(board, upper, lower, R, C)

    # 공기청정기(-1) 제외한 미세먼지 합
    total = 0
    for i in range(R):
        for j in range(C):
            if board[i][j] > 0:
                total += board[i][j]

    print(total)


if __name__ == "__main__":
    solve()
