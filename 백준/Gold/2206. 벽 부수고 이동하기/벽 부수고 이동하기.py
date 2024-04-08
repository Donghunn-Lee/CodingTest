# 벽 부수고 이동하기

# 그래프의 최단 경로라서 우선 고민 없이 bfs를 채택.
# 맵에 벽이 있고, 단 한 번, 한 개의 벽을 뚫고 지나갈 수 있다는 조건이 붙음.
# 그래서 deq에 넣는 튜플에 벽을 뚫었는지 여부를 체크하는 broke 변수를 넣음.

# 그렇게 풀리나 싶었는데, 벽을 뚫고 이동한 경로와 뚫지 않고 이동한 경로가 겹칠 경우 문제가 발생.
# 해법은 visited를 애초에 3차원 리스트로 만들어서 벽을 뚫은 경우와 뚫지 않은 경우의 값을 모두 저장하는 것.
# 3차원으로 만들어야 하나? 까진 스스로 생각했지만 적용시키기가 어려워 검색 후 답안 참고.

import sys
from collections import deque
input = sys.stdin.readline

def bfs(i, j, k):
    deq = deque()
    deq.append((i, j, k))

    # 벽 돌파 여부를 모두 체크하는 3차원 리스트로 생성.
    visited = [[[False] * 2 for _ in range(M)] for _ in range(N)]
    visited[i][j][k] = 1    # 시작 지점 초기화.

    while deq:
        ci, cj, broke = deq.popleft()

        # 목적지에 도달한 경우 해당 값을 리턴.
        if (ci, cj) == (N - 1, M - 1):
            return visited[ci][cj][broke]

        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni, nj = ci + di, cj + dj
            
            # 인덱스 범위 체크.
            if 0 <= ni < N and 0 <= nj < M:
                
                # 다음 칸이 갈 수 있는 길이고 아직 방문하지 않은 경우 deq에 추가.
                if graph[ni][nj] == '0' and not visited[ni][nj][broke]:
                    visited[ni][nj][broke] = visited[ci][cj][broke] + 1
                    deq.append((ni, nj, broke))

                # 다음 칸이 벽이며 아직 벽을 하나도 뚫지 않은 경우,
                # 벽을 뚫은 경로를 저정하는 visited[][][1]에 현재 경로의 값 + 1을 할당.
                # 이후 덱에도 기존 0이었던 broke가 아닌 1로 바꾸어 추가.
                # 이 때 추가된 튜플을 기점으로 visited[][][1]의 맵이 갱신되기 시작하여 [0]와 병행하여 탐색.
                elif graph[ni][nj] == '1' and not broke:
                    visited[ni][nj][1] = visited[ci][cj][broke] + 1
                    deq.append((ni, nj, 1))

    # 목적지에 도달하지 못하고 반복이 종료될 경우 -1을 리턴.
    return -1


if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = [list(input().rstrip()) for _ in range(N)]

    print(bfs(0, 0, 0))