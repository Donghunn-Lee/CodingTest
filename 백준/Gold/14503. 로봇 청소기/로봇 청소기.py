import sys
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    r, c, d = map(int, input().split())
    room = [list(map(int, input().split())) for _ in range(N)]

    # 북(0), 동(1), 남(2), 서(3)
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    cleaned = 0

    while True:
        # 1. 현재 칸 청소
        if room[r][c] == 0:
            room[r][c] = 2
            cleaned += 1

        found = False

        # 2. 네 방향 탐색 (왼쪽 회전)
        for _ in range(4):
            d = (d + 3) % 4  # 왼쪽 회전
            nr = r + dr[d]
            nc = c + dc[d]

            if room[nr][nc] == 0:
                r, c = nr, nc
                found = True
                break

        # 3. 네 방향 모두 청소 or 벽
        if not found:
            back_dir = (d + 2) % 4
            br = r + dr[back_dir]
            bc = c + dc[back_dir]

            if room[br][bc] == 1:
                break
            r, c = br, bc

    print(cleaned)

if __name__ == "__main__":
    solve()
