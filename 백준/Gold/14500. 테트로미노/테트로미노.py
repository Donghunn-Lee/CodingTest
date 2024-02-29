# 테트로미노
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]
dir = ((1, 0), (0, 1), (-1, 0), (0, -1))
visited = [[False] * M for _ in range(N)]       # dfs는 노드 맵
ans = 0
max_value = max(map(max, paper))
# Depth First Search
# 입력받은 좌표를 기반으로 가능한 모든 도형을 구성해 숫자 합의 최댓값을 전역 변수 ans에 저장.
def dfs(ci, cj, tmp ,n):
    global ans
    if n == 0:
        ans = max(ans, tmp)
    # 가지치기를 위해 tmp에 전체의 최댓값을 n번 곱한 결과가 ans보다 작을 경우, 이후 반복이 의미 없으므로 종료
    elif tmp + max_value * n < ans:
        return
    
    else:
        for d in dir:
            ni, nj = ci + d[0], cj + d[1]
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                visited[ni][nj] = True
                dfs(ni, nj, tmp + paper[ni][nj], n - 1)
                visited[ni][nj] = False

# 모자 모양 도형은 입력 좌표 기준 1칸 3방향을 동시에 고려해야하므로 따로 함수 구현
def hat_shape(ci, cj):
    global ans

    # 제외할 방향을 하나 결정해두고 다음 반복에서 나머지 3방향을 값을 계산
    for ex in dir:
        tmp = paper[ci][cj]     # 이렇게 현재 좌표값을 반복마다 초기화 해야 하는데 처음에 0을 할당해버려서 조금 방황함
        for d in dir:
            ni, nj = ci + d[0], cj + d[1]
            if d != ex:
                if 0 <= ni < N and 0 <= nj < M:
                    tmp += paper[ni][nj]
                else:
                    tmp = 0
                    break
                # 만약 3방향 중 한 곳이 없다면 0으로 초기화 후 break
        # 문제 없이 tmp 값을 보존했다면 max비교
        if tmp:
            ans = max(ans, tmp)

for i in range(N):
    for j in range(M):
        # 잊지 말고 시작노드도 True, False로 변경
        visited[i][j] = True
        dfs(i, j, 0, 4)
        visited[i][j] = False
        hat_shape(i, j)

print(ans)