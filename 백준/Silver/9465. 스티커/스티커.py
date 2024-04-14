# 스티커

import sys
input = sys.stdin.readline

def max_score_group(stickers):
    dp = [[0] * (N + 3) for _ in range(2)]

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
