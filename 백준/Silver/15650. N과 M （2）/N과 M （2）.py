# N과 M (2)

import sys
input = sys.stdin.readline

def dfs(start, count):
    global ans

    if count == M:
        ans.append(" ".join(map(str, seq)))
        return
    
    if start > N:
        return
    
    seq.append(start)
    dfs(start + 1, count + 1)
    seq.pop()

    dfs(start + 1, count)

if __name__ == "__main__":
    N, M = map(int, input().split())
    seq = []
    ans = []

    dfs(1, 0)

    print("\n".join(ans))