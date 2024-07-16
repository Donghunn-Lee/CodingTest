# RGB거리 2

# 전에 풀었던 rgb 거리 문제에서 처음과 끝의 조건이 추가된 문제.
# 처음 시작 RGB를 정해서 시작하고, 마지막에 처음과 다른 값들을 대상으로 최소 비용을 구함.
import sys
input = sys.stdin.readline
INF = 1e7

def sol():
    ans = INF

    for i in range(3):
        dp = [[INF] * 3 for _ in range(N)]
        dp[0][i] = rgb[0][i]

        for j in range(1, N):
            dp[j][0] = min(dp[j - 1][1], dp[j - 1][2]) + rgb[j][0]
            dp[j][1] = min(dp[j - 1][0], dp[j - 1][2]) + rgb[j][1]
            dp[j][2] = min(dp[j - 1][0], dp[j - 1][1]) + rgb[j][2]

        for j in range(3):
            if i != j:
                ans = min(ans, dp[-1][j])
    
    return ans

if __name__ == "__main__":
    N = int(input())
    rgb = [list(map(int, input().split())) for _ in range(N)]
    print(sol())