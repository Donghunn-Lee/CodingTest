# 바이러스

import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append(1)
    visited = [False] * (N + 1)
    count = 0

    visited[1] = True
    
    while q:
        s = q.popleft()

        for i in network[s]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                count += 1
    
    return count

if __name__ == "__main__":
    N = int(input())
    M = int(input())

    network = [[] for _ in range(N + 1)]
    
    for _ in range(M):
        a, b = map(int, input().split())
        network[a].append(b)
        network[b].append(a)

    print(bfs())