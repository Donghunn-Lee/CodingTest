# 16234 인구 이동

# 처음에 아무 생각 없이 dfs로 풀고 생각보다 쉽네 하고 넘어갔는데, 당황 스러운 시간초과.
# bfs로 바꿔봤는데 여전히 시간초과
# 놓치고 있던 부분은 전날 변경된 버전을 다음 날에 적용시키는 것이 아니라,
# '전날 변경된 것'만 다음 날 조사 대상으로 넘기는 것이었음

from collections import deque
import sys
input = sys.stdin.readline

N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

visited = [[-1]*N for _ in range(N)]
day = 0

candidates = [(i, j) for i in range(N) for j in range(N)]

while True:
    moved = False
    next_candidates = []

    for i, j in candidates:
        if visited[i][j] == day:
            continue

        q = deque([(i, j)])
        visited[i][j] = day
        union = [(i, j)]
        total = A[i][j]

        while q:
            x, y = q.popleft()
            cur = A[x][y]

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                if visited[nx][ny] == day:
                    continue

                diff = cur - A[nx][ny]
                if diff < 0:
                    diff = -diff
                if diff < L or diff > R:
                    continue

                visited[nx][ny] = day
                q.append((nx, ny))
                union.append((nx, ny))
                total += A[nx][ny]

        if len(union) > 1:
            moved = True
            avg = total // len(union)
            for x, y in union:
                A[x][y] = avg
            # 🔑 인구가 바뀐 칸만 다음 날 후보
            next_candidates.extend(union)

    if not moved:
        break

    candidates = next_candidates
    day += 1

print(day)
