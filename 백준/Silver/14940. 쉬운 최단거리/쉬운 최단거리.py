# 쉬운 최단거리

# 출발점에서 모든 지점으로의 거리를 구해야 하므로, 출발점에서 퍼져나가는 bfs 문제로 판단.
# 방문체크와 거리를 각각의 2차원 리스트로 체크해야 함.
# 땅인데 갈 수 없는 곳이면 -1 이라는 조건을 늦게 확인해서 시간 잡아먹음.
import sys
from collections import deque
input = sys.stdin.readline
INF = 1e9

def bfs():
    si, sj = 0, 0

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 2:
                si, sj = i, j
                dist[i][j] = 0

            elif graph[i][j] == 0:
                dist[i][j] = 0

    deq = deque()
    deq.append((si, sj))
    visited = [[0] * M for _ in range(N)]

    while deq:
        ci, cj = deq.popleft()

        for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            ni, nj = ci + di, cj + dj

            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                if graph[ni][nj] == 1:
                    visited[ni][nj] = 1
                    deq.append((ni, nj))
                    dist[ni][nj] = dist[ci][cj] + 1


if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    dist = [[-1] * M for _ in range(N)]
    ans = []

    bfs()

    for i in range(N):
        ans.append(" ".join(map(str, dist[i])))
    
    print("\n".join(ans))