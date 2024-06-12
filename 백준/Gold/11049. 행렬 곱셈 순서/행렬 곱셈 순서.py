# 행렬 곱셈 순서

# 혼자서는 정말 하루 반나절은 쏟아야 간신히 풀까 말까 한 문제.
# 우선 dp문제는 맞음. 1부터 N까지의 행렬 중 곱셈 순서를 정해야 하고, 행렬 곱의 방향은 정해져 있음.
# 때문에 행렬 두 개의 곱을 모두 구하고, 이를 기반으로 3개의 곱을 구하는 방식으로 점화식이 짜여진다는 것은 알겠으나
# 그 과정을 구현하는 게 어려웠음.

# 핵심은 어차피 작은 길이부터 계산한 값이 메모이제이션된다는 것.
# cur -> j, (j + 1) -> (cur + term)의 범위 안의 최소 연산 수를 뽑고, 그 다음 양쪽의 행렬 곱 연산을 진행함.
# 범위 안의 값을 dp테이블에서 가져옴으로써 시간 효율을 얻을 수 있음.

import sys
input = sys.stdin.readline

def sol():
    dp = [[0] * N for _ in range(N)]

    # 길이 1부터 N까지의 경우를 계산.
    for term in range(1, N):

        # 각 탐색의 시작값.
        for cur in range(N):
            if cur + term == N:     # 범위 이탈시 중지.
                break

            # 초깃값 할당.
            dp[cur][cur + term] = 1e9

            # 기준점을 옮겨가며 범위 안을 2등분. 최소 연산 수 갱신.
            for j in range(cur, cur + term):
                dp[cur][cur + term] = min(dp[cur][cur + term], dp[cur][j] + dp[j + 1][cur + term] + matrix[cur][0] * matrix[j][1] * matrix[cur + term][1])

    return dp[0][N - 1]


if __name__ == "__main__":
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    print(sol())