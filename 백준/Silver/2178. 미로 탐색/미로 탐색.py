# 미로 탐색

# 방향 조건만 보고 dfs로 풀어버렸는데, 결국 최단 거리를 구하는 문제라는 사실을 간과함.
# bfs로 다시 풀 수밖에 없었음. 탐색 문제에서 최단 문제인지 먼저 확인하고 조건을 보는 습관을 가질 것.
import sys
from collections import deque
input = sys.stdin.readline

# 방법은 전형적인 bfs 문제와 별반 다르지 않았음. count 리스트 방식이 최근 몇 번 쓰고 있는 방식. 그냥 dp임.
def bfs():
    q = deque()
    q.append((0, 0))
    visited = [[False] * M for _ in range(N)]
    count = [[0] * M for _ in range(N)]
    count[0][0] = 1

    while q:
        ci, cj = q.popleft()

        for d in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni, nj = ci + d[0], cj + d[1]
            
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                if maze[ni][nj] == '1':
                    if (ni, nj) == (N - 1, M - 1):
                        return count[ci][cj] + 1
                    visited[ni][nj] = True
                    count[ni][nj] = count[ci][cj] + 1
                    q.append((ni, nj))

    return count[-1][-1]

if __name__ == "__main__":
    N, M = map(int, input().split())
    maze = [list(input().rstrip()) for _ in range(N)]

    print(bfs())