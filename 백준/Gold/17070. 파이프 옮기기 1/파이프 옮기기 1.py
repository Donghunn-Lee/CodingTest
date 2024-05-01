# 파이프 옮기기 1

# 처음에 단순한 그래프 문제인줄 알고 보다가, 결국 한 점에 도달하는 모든 경우의 수 이므로 dfs가 더 효율적이라고 판단.
# dfs로 풀고 pypy3로 제출하니 조금 느리지만 통과는 됐음. 다만 python으로 제출하니 시간초과.
# 찾아보니 dp로 풀어야 하는 문제였음. 가능한 코드는 보지 않고 해설만 읽으며 다시 풀어서 간신히 제출함.
# 풀이는 3차원 dp테이블을 사용해서 각각 가로, 세로, 끝 점이 현 위치에 놓일 수 있는 이전 칸의 경우들을 계산해 저장함.
# dp는 상향식 하향식 생각하는 것부터 일이지만, 점화식을 구축하는 게 단순한 문제라도 그리 쉽게 떠오르지 않는 것 같음.

import sys
input = sys.stdin.readline

def DP():
    # 가로, 세로, 대각선 끝이 놓일 수 있는 수의 dp 테이블 생성.
    dp_table = [[[0, 0, 0] for _ in range(N + 1)] for _ in range(N + 1)]
    dp_table[1][2] = [1, 0, 0]    # 시작 파이프는 항상 1,2에 끝이 놓인 가로 형태.

    # 현 위치로 가로, 세로, 대각선 끝을 옮길 수 있는 이전 형태의 수들을 계산.
    for i in range(1, N + 1):
        for j in range(3, N + 1):

            # 벽이 아닌 빈 공간인 경우.
            if graph[i][j] == 0:
                dp_table[i][j][0] = dp_table[i][j - 1][0] + dp_table[i][j - 1][2]   # 왼쪽 칸의 가로, 대각선 끝.
                dp_table[i][j][1] = dp_table[i - 1][j][1] + dp_table[i - 1][j][2]   # 위쪽 칸의 세로, 대각선 끝.
                
                # 빈 공간이면서 왼쪽, 위쪽 칸도 벽이 아닌 경우에만 대각선 계산.
                if graph[i - 1][j] == 0 and graph[i][j - 1] == 0:
                    dp_table[i][j][2] = sum(dp_table[i - 1][j - 1]) # 왼쪽 위 칸에 끝이 놓은 모든 경우의 합.

    return sum(dp_table[N][N])


if __name__ == "__main__":
    N = int(input())
    graph = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
    
    print(DP())