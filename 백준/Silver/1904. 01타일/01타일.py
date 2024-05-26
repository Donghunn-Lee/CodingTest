# 01타일

import sys
input = sys.stdin.readline

def sol(n):
    dp = [0] * (n + 1)
    dp[:2] = [1] * 2

    for i in range(2, n + 1):
        dp[i] = sum(dp[i - 2: i]) % 15746
    
    return dp[n]


if __name__ == "__main__":
    N = int(input())

    print(sol(N))