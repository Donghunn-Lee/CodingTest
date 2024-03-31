# 파티

# 다익스트라 알고리즘... 뭔지는 알고 있었지만 문제유형으로는 처음 봐서 전혀 감을 잡지 못함.
# 그저 그래프 문제로 생각하고 dfs일지 bfs일지 고민하다가 bfs로 붙잡고 한 세월을 보냄.
# bfs로도 분명 풀릴 것은 같은데 아마 시간초과가 나지 않을까 싶음.

# +++ 늦어서 대충 보고 다시 문제를 이해하려고 살펴보니 그냥 다익스트라가 필요한 문제라는 것을 알았음.
# 단방향 엣지, a에서 b로 가는 최단 경로를 구할 때의 경우에 다익스트라를 기억하자. 벨만 포드 알고리즘도 알아야 할 듯함.
# 또 참고한 답안은 모든 노드에서 X로 가는 최단 거리를 구할 때, 다익스트라를 N - 1번 쓰지 않고, 시간을 줄이기 위해
# 역방향 엣지 그래프를 새로 만들어서 X에서 다른 모든 노드로 가는 최단 거리를 구하는 문제로 바꾸었음.

import sys, heapq
input = sys.stdin.readline
INF = 1e10

def dijkstra(start, edge):
    distance = [INF] * (N + 1)
    q = []
    heapq.heappush(q, (start, 0))

    while q:
        ci, cd = heapq.heappop(q)

        if distance[ci] >= cd:
            for ni, nd in edge[ci]:
                if distance[ni] > cd + nd:
                    distance[ni] = cd + nd
                    heapq.heappush(q, (ni, cd + nd))

    return distance


if __name__ == "__main__":
    N, M, X = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    reverse_graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        reverse_graph[b].append((a, c))
    
    go_to = dijkstra(X, reverse_graph)
    come_back = dijkstra(X, graph)

    print(max([go_to[i] + come_back[i] for i in range(1, N + 1) if i != X]))