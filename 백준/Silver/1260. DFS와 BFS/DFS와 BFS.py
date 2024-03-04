# DFS와 BFS
import sys
from collections import deque
input = sys.stdin.readline

def DFS(graph, visited, start, count):
    global ans_dfs
    if count == 1:
        return
    
    for i in graph[start]:
        if not visited[i]:
            ans_dfs.append(i)
            visited[i] = True
            DFS(graph, visited, i, count - 1)
            

def BFS(graph, start):
    global ans_bfs
    q = deque()
    q.append(start)
    visited = [start]

    while q:
        cur = q.popleft()

        for i in graph[cur]:
            if i not in visited:
                ans_bfs.append(i)
                q.append(i)
                visited.append(i)

if __name__ == "__main__":
    N, M, V = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1)
    ans_dfs = [V]
    ans_bfs = [V]
    
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    for i in range(1, N + 1):
        graph[i].sort()
    
    visited[V] = True
    DFS(graph, visited, V, N)
    BFS(graph, V)

    print(' '.join(map(str, ans_dfs)))
    print(' '.join(map(str, ans_bfs)))
    
