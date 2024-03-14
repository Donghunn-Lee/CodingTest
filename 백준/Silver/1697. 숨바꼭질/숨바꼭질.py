# 숨바꼭질

import sys
from collections import deque
input = sys.stdin.readline

def bfs(n, k):
    q = deque()
    q.append(n)
    visited = [False] * (100001)
    distance = {n : 0, k : 0}
    if n == k:
        return 0
    
    while q:
        ci = q.popleft()
        gap = [ci + 1, ci - 1, ci * 2]
        for ni in gap:
            if 0 <= ni < 100001:
                if not visited[ni]:
                    q.append(ni)
                    visited[ni] = True
                    distance[ni] = distance[ci] + 1

        if visited[k]:
            return distance[k]

if __name__ == "__main__":
    N, K = map(int, input().split())
    print(bfs(N, K))