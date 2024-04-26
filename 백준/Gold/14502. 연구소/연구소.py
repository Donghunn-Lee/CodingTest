# 연구소

import sys
from collections import deque
input = sys.stdin.readline

def location(graph):
    virus = []
    empty_space = []

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 2:
                virus.append((i, j))
            elif graph[i][j] == 0:
                empty_space.append((i, j))

    return virus, empty_space

def bfs(num_empty):
    global ans

    deq = deque(virus)
    visited = [[0] * M for _ in range(N)]
    infected_space = 0

    while deq:
        ci, cj = deq.popleft()

        for d in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ni, nj = ci + d[0], cj + d[1]

            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0:
                if laboratory[ni][nj] == 0:
                    infected_space += 1
                    visited[ni][nj] = 1
                    deq.append((ni, nj))
    
    ans = max(ans, num_empty - infected_space - 3)

def dfs(cur, count, limit):
    if count == 3:
        bfs(limit)
        return
    
    if cur == limit:
        return
    
    i, j = empty_space[cur]

    laboratory[i][j] = 1
    dfs(cur + 1, count + 1, limit)
    laboratory[i][j] = 0

    dfs(cur + 1, count, limit)
    



if __name__ == "__main__":
    N, M = map(int, input().split())
    laboratory = [list(map(int, input().split())) for _ in range(N)]
    virus, empty_space = location(laboratory)
    ans = 0

    dfs(0, 0, len(empty_space))

    print(ans)