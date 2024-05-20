# 줄 세우기

import sys
from collections import deque
input = sys.stdin.readline

def topology_sort():
    q = deque()

    for s in range(1, N + 1):
        if inDegree[s] == 0:
            q.append(s)

    while q:
        s = q.popleft()
        ans.append(s)
        
        for nxt in graph[s]:
            inDegree[nxt] -= 1
            if inDegree[nxt] == 0:
                q.append(nxt)

    print(*ans, sep=" ")


if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    inDegree = [0] * (N + 1)
    ans = []

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        inDegree[b] += 1
    
    topology_sort()
