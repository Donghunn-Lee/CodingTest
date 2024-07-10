# 벽 부수고 이동하기 4

# 기존 벽 부수고 이동하기는 벽을 부순 경우와 부수지 않은 경우를 고려해야해서 복잡했는데, 이 문제는 그보단 덜 한듯?
# 단순한 완전탐색으로 벽을 발견할 때마다 bfs를 돌리면 답을 구할 순 있겠지만, 절대 시간 내에 풀지는 못한다고 판단.
# 때문에 먼저 한 번 돌려서 현재 벽으로 나뉘어진 이동할 수 있는 인접한 칸들의 수를 구해 구역을 생성하는 방법을 사용.

# 먼저 전제 graph에서 인접한 모든 이동 가능한 칸을 section으로 구분하고, visited에 sections 번호를 할당함.
# section 번호마다 해당 section내 칸의 수를 딕셔너리로 저장. dp테이블이 되는 셈.
# section을 모두 구한 다음, 다시 완전탐색으로 벽을 찾고, 해당 벽과 인접한 구역을 visited로 찾아 칸의 수를 더함.

import sys
from collections import deque
input = sys.stdin.readline

# 구역 구하기.
def find_section(si, sj):
    global section_num  # 구역 번호

    deq = deque()
    deq.append((si, sj))
    count = 1   # 현재 칸 포함

    while deq:
        ci, cj = deq.popleft()

        for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            ni, nj = ci + di, cj + dj

            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and graph[ni][nj] == '0':

                # 현재 bfs로 탐색 가능한 visited의 모든 칸에 구역 번호를 할당.
                visited[ni][nj] = section_num
                deq.append((ni, nj))
                count += 1
    
    return count

# 벽을 부쉈을 때 이동할 수 있는 칸을 계산.
def if_broken(si, sj):
    count = 1
    visited_4way = set()    # 벽 하나를 같은 구역의 칸이 여러 개 인접한 경우를 대비.

    for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
        ni, nj = si + di, sj + dj

        # 벽과 인접한 이동 가능한 칸이면서 아직 만나지 못한 구역인 경우.
        if 0 <= ni < N and 0 <= nj < M and graph[ni][nj] == '0' and visited[ni][nj] not in visited_4way:
            visited_4way.add(visited[ni][nj])

            # 딕셔너리에서 해당 구역 내 칸 수를 더해줌.
            # 이미 구한 구역들을 활용해 시간을 효율적으로 줄일 수 있음.
            count += section[visited[ni][nj]]
    
    return count
            

if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = [input().rstrip() for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    section = dict()
    section_num = 0
    ans = [[0] * M for _ in range(N)]

    # 구역과 구역 내 칸 수 구하기.
    for i in range(N):
        for j in range(M):
            if graph[i][j] == '0' and not visited[i][j]:
                section_num += 1
                visited[i][j] = section_num
                section[section_num] = find_section(i, j)
    
    # 벽을 부수고 이동 가능한 모든 칸 수를 section을 사용해 계산.
    for i in range(N):
        for j in range(M):
            if graph[i][j] == '1':
                ans[i][j] = if_broken(i, j) % 10

    print("\n".join(map(lambda x : "".join(map(str, x)), ans)))
