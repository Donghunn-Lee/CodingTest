# 트리의 지름  (2번째?)

# 전에 풀었던 트리의 지름이랑 이름도 똑같아서 정말 같은 문제인가? 싶었는데 같은 문제같음.
# 입력 방식만 조금 다르지, 트리에 노드 수를 주고 양방향 간선과 가중치(거리)를 주고, 트리의 지름을 구하는 같은 문제.
# 복붙해서 좀만 고칠까 하다가 그냥 다시 풀어 봐야겠다는 생각으로 다시 풀었음.
# 트리의 임의의 한 정점에서 최대 거리에 있는 정점은, 트리의 지름을 이루는 양 정점 중 하나라는 규칙을 이용해야함.
import sys
sys.setrecursionlimit(15000)
input = sys.stdin.readline

def dfs(graph, visited, start, dist):
    global diameter, node
    
    if diameter < dist:
        diameter, node = dist, start

    visited[start] = True

    for i, j in graph[start]:
        if not visited[i]:
            dfs(graph, visited, i, dist + j)


if __name__ == "__main__":
    N = int(input())
    graph = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1)
    diameter, node = 0, 0
    
    for _ in range(N - 1):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    dfs(graph, visited, 1, 0)
    
    visited = [False] * (N + 1)
    diameter = 0

    dfs(graph, visited, node, 0)

    print(diameter)