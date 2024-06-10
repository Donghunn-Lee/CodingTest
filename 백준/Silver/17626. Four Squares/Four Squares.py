# Four Squares

import sys
input = sys.stdin.readline

def sol():
    dp = [0] * (N + 1)
    dp[1] = 1

    for i in range(1, N + 1):
        min_num = 1e6

        for j in range(1, int(i ** 0.5) + 1):
            min_num = min(min_num, dp[i - j ** 2])
        
        dp[i] = min_num + 1

    return dp[N]


if __name__ == "__main__":
    N = int(input())
    print(sol())