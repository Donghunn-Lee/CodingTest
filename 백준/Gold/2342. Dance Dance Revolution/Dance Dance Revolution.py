# Dance Dance Revolution

# dfs로 호기롭게 풀다가 시간초과.
# n이 
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def move(a, b):
    if a == b:
        return 1
    
    elif a == 0:
        return 2
    
    elif abs(b - a) % 2 == 0:
        return 4
    
    else:
        return 3



def solve(n, l, r):
    if n >= len(seq)-1:
        return 0
 
    if dp[n][l][r] != -1:
        return dp[n][l][r]
 
    dp[n][l][r] = min(solve(n+1, seq[n],r) + move(l, seq[n]), solve(n+1, l, seq[n]) + move(r, seq[n]))
    return dp[n][l][r]


if __name__ == "__main__":
    seq = list(map(int, input().split()))
    dp = [[[-1]*5 for _ in range(5)] for _ in range(100000)]
    
    print(solve(0, 0, 0))