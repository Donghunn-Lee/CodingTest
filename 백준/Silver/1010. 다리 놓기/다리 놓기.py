# 다리 놓기

import sys, math
input = sys.stdin.readline

if __name__ == "__main__":
    T = int(input())
    ans = []

    for _ in range(T):
        n, m = map(int, input().split())
        bridge = math.factorial(m) // (math.factorial(n) * math.factorial(m - n))
        ans.append(str(bridge))
    
    print("\n".join(ans))