# 퇴사

import sys
input = sys.stdin.readline

def best_schedule(cl):
    dp = [0] * (N + 2)
   
    for i, (t, p) in enumerate(cl):
        if i + t <= N:
            dp[i + t] = max(dp[i + t], max(dp[:i + 1]) + p)

    return max(dp)
            
if __name__ == "__main__":
    N = int(input())
    consulution_list = [list(map(int, input().split())) for _ in range(N)]

    print(best_schedule(consulution_list))