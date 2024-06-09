# 경로 찾기

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

def dfs(si, ci):
    for j in range(N):
        if graph[ci][j] == 1 and not visited[ci][j]:
            graph[si][j] = 1
            visited[ci][j] = 1
            dfs(si, j)
        

if __name__ == "__main__":
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    ans = []

    for i in range(N):
        visited = [[0] * N for _ in range(N)]
        dfs(i, i)
    
    for i in range(N):
        ans.append(" ".join(map(str, graph[i])))
    
    print("\n".join(ans))
