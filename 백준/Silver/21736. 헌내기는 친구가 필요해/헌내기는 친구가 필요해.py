# 헌내기는 친구가 필요해

import sys
from collections import deque
input = sys.stdin.readline

def bfs(si, sj):
    deq = deque([(si, sj)])
    visited = [[0] * M for _ in range(N)]
    people = 0

    while deq:
        ci, cj = deq.popleft()

        for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            ni, nj = ci + di, cj + dj

            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                if graph[ni][nj] != "X":
                    if graph[ni][nj] == "P":
                        people += 1
                    
                    deq.append((ni, nj))

                visited[ni][nj] = 1

    if people:
        return people
    
    else:
        return "TT"


if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = [input().rstrip() for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if graph[i][j] == "I":
                print(bfs(i, j))
                exit()