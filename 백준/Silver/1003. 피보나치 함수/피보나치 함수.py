# 피보나치 함수

import sys
input = sys.stdin.readline

def fibonacci_DP(n):
    if n in dp:
        return dp[n]
    
    tmp1, tmp2 = fibonacci_DP(n - 1), fibonacci_DP(n - 2)
    dp[n] = [tmp1[0] + tmp2[0], tmp1[1] + tmp2[1]]

    return dp[n]


if __name__ == "__main__":
    T = int(input())
    
    result = []
    for t in range(T):
        N = int(input())
        dp = {0 : [1, 0], 1 : [0, 1]}
        tmp = fibonacci_DP(N)
        result.append(f"{tmp[0]} {tmp[1]}")

    print("\n".join(result))