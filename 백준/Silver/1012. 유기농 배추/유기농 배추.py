# 유기농 배추

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)
# dfs와 bfs 두 방법 모두 무리없이 적용 가능한 문제라고 생각, 고심끝에 덜 익숙한 dfs를 사용.
# 입력받은 좌표를 기준으로 상하좌우를 탐색하여 배추 위치를 찾음.
# 그 다음 visited에 True로 표시하여 배추 군집을 찾아 표시하는 함수.
def dfs(farm, ci, cj, visited):
    for d in dir:
        ni, nj = ci + d[0], cj + d[1]

        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
            if farm[ni][nj] == 1:
                visited[ni][nj] = True
                dfs(farm, ni, nj, visited)


if __name__ == "__main__":
    T = int(input())
    dir = ((1, 0), (0, 1), (-1, 0), (0, -1))
    ans = []

    for t in range(T):
        M, N, K = map(int, input().split())
        farm = [[0 for _ in range(M)] for _ in range(N)]
        visited = [[False for _ in range(M)] for _ in range(N)]
        count = 0
        
        for _ in range(K):
            j, i = map(int, input().split())
            farm[i][j] = 1
        
        # 전체 좌표를 돌며 배추가 있는 곳을 찾음.
        # 그곳은 우선 배추흰지렁이가 1마리는 들어가므로 count에 1을 더하고, visited를 True로 변경
        # dfs 함수가 한 번 실행되면 해당 배추의 군집은 모두 확인된 것이므로, 방문하지 않은 좌표를 다시 탐색.
        for i in range(N):
            for j in range(M):
                if farm[i][j] == 1 and not visited[i][j]:
                    count += 1
                    visited[i][j] = True
                    dfs(farm, i, j, visited)
        
        ans.append(count)
    
    print("\n".join(map(str, ans)))
        
