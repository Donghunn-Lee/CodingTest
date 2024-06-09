# 경로 찾기

# 직관적으로 이해는 되는데 값을 갱신하는 과정이 조금 햇갈렸던 문제.
# dfs나 bfs 모두 사용 가능했음. 나는 처음부터 dfs를 생각했기에 dfs를 사용.
# 풀긴 했는데 시간이 너무 길어서, 제대로 된 방법을 검색.
# visited를 그냥 1차원으로 해서 현재 탐색의 시작노드만 가지고 값을 갱신하는 방법이 있었음.

import sys
input = sys.stdin.readline

def dfs(i):
    for j in range(N):
        if graph[i][j] == 1 and not visited[j]:
            visited[j] = 1
            dfs(j)

if __name__ == "__main__":
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    ans = []

    for i in range(N):
        visited = [0 for _ in range(N)]
        dfs(i)
        ans.append(" ".join(map(str, visited)))
    
    print("\n".join(ans))