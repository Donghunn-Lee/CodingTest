# 다리 놓기

# 실버 5 dp문제. 그런데도 난 쉽게 점화식을 떠올리지 못함.
# 검색해서 본 이 문제의 해설을 보며 내가 dp를 풀 때 중대한 것을 간과하고 있다는 사실을 깨달음.
# 그것은 점화식을 구상할 때 표를 그려보지 않는 다는 것.
# 해설에선 n과 m의 값들에 대한 표가 작성되어 있었고, 그 표를 기준으로 dp테이블을 상향식으로 채워가는 점화식을 구성함.
# 앞으로 dp 문제를 풀 땐 표를 작성하자.
import sys
input = sys.stdin.readline

def sol(n, m) :
    dp = [[1] * (m + 1) for _ in range(m + 1)]

    for i in range(2, m + 1):
        dp[1][i] = i

    for i in range(2, n + 1):
        for j in range(i + 1, m + 1):
            dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]

    return dp[n][m]

if __name__ == "__main__":
    T = int(input())
    ans = []

    for _ in range(T):
        N, M = map(int, input().split())
        ans.append(str(sol(N, M)))
    
    print("\n".join(ans))