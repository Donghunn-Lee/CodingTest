# 스티커

# 역시 dp는 실버여도 그리 쉽진 않구나 싶었던 문제.
# 그래도 2행 n열에 점화식으로 더해가는 단순한 구조라 풀 수 있었음.
# 재귀로도 문제 없이 풀릴 것 같았지만 가급적 for문으로 풀고 싶어서 그렇게 함.

import sys
input = sys.stdin.readline

def max_score_group(stickers):
    dp = [[0] * (N + 3) for _ in range(2)]

    # 전형적인 dp점화식으로, 현재 지점에서 더할 수 있는 바로 다음 수들을 모두 더해가며 dp리스트에 최댓값을 갱신.
    for j in range(N + 1):
        dp[1][j + 2] = max(dp[1][j + 2], dp[0][j] + stickers[1][j + 2])
        dp[0][j + 2] = max(dp[0][j + 2], dp[1][j] + stickers[0][j + 2])
        dp[1][j + 1] = max(dp[1][j + 1], dp[0][j] + stickers[1][j + 1])
        dp[0][j + 1] = max(dp[0][j + 1], dp[1][j] + stickers[0][j + 1])

    return max(map(max, dp))
    
if __name__ == "__main__":
    T = int(input())
    ans = []

    for _ in range(T):
        N = int(input())
        stickers = [[0] * 2 + list(map(int, input().split())) + [0] for _ in range(2)]
        ans.append(max_score_group(stickers))
    
    print('\n'.join(map(str, ans)))
