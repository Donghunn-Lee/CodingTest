# 연구소

# 벽을 세울 수 있는 모든 조합을 찾고, 그 다음 바이러스의 위치에서 탐색을 통해 안전한 공간의 수를 세야 하는 문제.
# 아마 모듈로 조합을 뽑을 수도 있을텐데, dfs로 해도 시간 초과가 안 나는지 확인하기 위해 dfs를 사용. 통과됨.
# 백준에서 dfs와 bfs를 같이 쓰는 문제는 처음이지만(bfs 대신 dfs를 또 써도 되긴 할 텐데) 골드 4라 크게 어렵진 않았음.

import sys
from collections import deque
input = sys.stdin.readline

# 바이러스와 빈 공간의 위치 정보를 얻기 위한 함수.
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

# dfs에서 만든 조합으로 벽을 막은 상태에서 바이러스 전파를 시뮬레이션.
def simulation(num_empty):
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

# 3개의 벽을 세울 수 있는 모든 조합을 찾고, 조합이 완성될 때마다 바이러스 전파 시뮬레이션을 돌리는 함수.
def build_wall(cur, count, limit):
    if count == 3:
        simulation(limit)
        return
    
    if cur == limit:
        return
    
    i, j = empty_space[cur]

    laboratory[i][j] = 1
    build_wall(cur + 1, count + 1, limit)
    laboratory[i][j] = 0

    build_wall(cur + 1, count, limit)
    



if __name__ == "__main__":
    N, M = map(int, input().split())
    laboratory = [list(map(int, input().split())) for _ in range(N)]
    virus, empty_space = location(laboratory)
    ans = 0

    build_wall(0, 0, len(empty_space))

    print(ans)