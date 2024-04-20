# 등산로 조성

# 처음엔 백준의 '벽 부수고 넘어가기' 문제와 유사하다 생각하여 산을 깎은 경우를 가정해 3차원 visited를 만듦.
# 그러나 풀다 보니 산을 깎음의 유무만이 아니라 그 정도까지 계산해야 하므로 graph를 건드려야 함을 인지.
# 그래서 dfs이니 graph의 값을 바꾸고 백 트레킹으로 복구하고, 이 때 visited도 3차원이 아닌 2차원을 사용.
# 그렇게만 바꾸니까 풀렸음. 벽 부수고 넘어가기에서 꽤나 골치 아팠던 기억이 있어, 이를 피하고자 했던 것인데
# 아직 내 문제 파악 능력이 그리 좋지 못하다는 반증이 되었음.

def dfs(ci, cj, cutted, length):
    # 최대 길이를 도출할 max_length.
    # 이 값을 어디서 초기화시킬 종료지점을 찾지 못해 그냥 매번 초기화.
    global max_length
    max_length = max(max_length, length)

    # visited 체크. 함수 종료시 백 트레킹.
    visited[ci][cj] = 1

    for di, dj in dir:
        ni, nj = ci + di, cj + dj

        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
            # 현재 위치보다 더 낮은 곳인 경우 재귀 호출.
            if graph[ci][cj] > graph[ni][nj]:
                dfs(ni, nj, cutted, length + 1)

            # 이미 낮아서 갈 수 있는 곳은 깎아도 의미가 없으므로, 더 높아서 갈 수 없을 때만 깎음.
            else:
                # 더 낮으면서도 아직 산을 깍은 적이 없는 루트의 경우.
                if not cutted:
                    # 매 케이스마다 깎을 수 있는 수치가 주어지므로 모든 값을 대입.
                    for i in range(1, K + 1):
                        if graph[ci][cj] > graph[ni][nj] - i:
                            # graph값 자체를 바꾸며 백 트레킹.
                            graph[ni][nj] -= i
                            dfs(ni, nj, True, length + 1)
                            graph[ni][nj] += i
    
    visited[ci][cj] = 0


if __name__ == "__main__":
    T = int(input())
    output = []
    
    for t in range(1, T + 1):
        N , K = map(int, input().split())
        graph = [list(map(int, input().split())) for _ in range(N)]
        visited = [[0] * N for _ in range(N)]
        dir = ((1, 0), (0, 1), (-1, 0), (0, -1))
        max_length = 0
        max_height = max(map(lambda x : max(x), graph[:]))  # 시작점이 될 최고 높이 봉우리들 찾기.

        for i in range(N):
            for j in range(N):
                # 가장 높은 봉우리중 하나인 경우 함수 실행.
                if graph[i][j] == max_height:
                    dfs(i, j, False, 1)
        
        output.append(f'#{t} {max_length}')
    
    print("\n".join(output))