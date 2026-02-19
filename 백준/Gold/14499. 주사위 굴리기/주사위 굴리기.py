import sys
input = sys.stdin.readline

def solve():
    N, M, x, y, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    cmds = list(map(int, input().split()))

    # 0: 위, 1: 아래, 2: 북, 3: 남, 4: 서, 5: 동
    dice = [0] * 6

    # 동, 서, 북, 남
    dx = [0, 0, 0, -1, 1]
    dy = [0, 1, -1, 0, 0]

    for cmd in cmds:
        nx = x + dx[cmd]
        ny = y + dy[cmd]

        if not (0 <= nx < N and 0 <= ny < M):
            continue

        t, b, n, s, w, e = dice

        if cmd == 1:      # 동
            dice = [w, e, n, s, b, t]
        elif cmd == 2:    # 서
            dice = [e, w, n, s, t, b]
        elif cmd == 3:    # 북
            dice = [s, n, t, b, w, e]
        else:             # 남
            dice = [n, s, b, t, w, e]

        if board[nx][ny] == 0:
            board[nx][ny] = dice[1]
        else:
            dice[1] = board[nx][ny]
            board[nx][ny] = 0

        print(dice[0])
        x, y = nx, ny

if __name__ == "__main__":
    solve()
