# 연결 요소의 개수

def dfs(graph, v, visited):
    visited[v] = True
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1)
    count = 0

    for i in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    for i in range(1, N + 1):
        if not visited[i]:
            dfs(graph, i, visited)
            count += 1

    print(count)