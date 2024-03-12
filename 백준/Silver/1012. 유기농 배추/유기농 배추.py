# 유기농 배추

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

# dfs와 bfs 두 방법 모두 무리없이 적용 가능한 문제라고 생각, 고심끝에 덜 익숙한 dfs를 사용.
# 입력받은 좌표를 기준으로 상하좌우를 탐색하여 배추 위치를 찾음.
# 찾은 좌표의 값은 0으로 바꿔줌으로써 visited 맵을 만들어 사용 할 필요가 없음.
def dfs(farm, ci, cj):
    for d in dir:
        ni, nj = ci + d[0], cj + d[1]

        if 0 <= ni < N and 0 <= nj < M and farm[ni][nj] == 1:
            farm[ni][nj] = 0
            dfs(farm, ni, nj)


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
        # 그곳은 우선 배추흰지렁이가 1마리는 들어가므로 count에 1을 더함.
        # 다시 방문하지 않도록 해당 좌표 값을 0으로 재할당.
        # dfs 함수가 한 번 실행되면 해당 배추의 군집은 모두 확인된 것이므로, 다른 군집을 찾아 반복.
        for i in range(N):
            for j in range(M):
                if farm[i][j] == 1:
                    count += 1
                    dfs(farm, i, j)
        
        ans.append(count)
    
    print("\n".join(map(str, ans)))
        
