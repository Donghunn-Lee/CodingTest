# 돌 게임

import sys
input = sys.stdin.readline

def stone_game(n):
    dp = [0] * (n + 3)
    dp[1] = 1
    dp[2] = 0
    dp[3] = 1

    for i in range(4, n + 1):
        if dp[i - 1]:
            dp[i] = 0
        else:
            dp[i] = 1

    if dp[n]:
        return 'SK'
    
    else:
        return 'CY'

if __name__ == "__main__":
    N = int(input())

    print(stone_game(N))