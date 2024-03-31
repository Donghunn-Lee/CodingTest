# 특정한 최단 경로

# 직전 문제로 다익스트라를 풀어봤기 때문에, 바로 다익스트라 문제임을 파악할 수 있었음.
# 다만 경유지가 새로 생겨서 어찌 해야 하나 보니, 경유지를 시작점으로 해서 최단 경로를 각각 구하는 방법을 생각함.
# 경우의 수는 1 -> 경유1 -> 경유2 -> N, 1 -> 경유2 -> 경유1 -> N 이렇게 두 가지 뿐.
# 30분 조금 넘겨서 풀 수 잇었는데, 반례가 너무 까다로워서 찾느라 좀 더 걸림.
import sys, heapq
input = sys.stdin.readline
INF = 1e10

# 다익스트라 알고리즘.
def dijkstra(start, edge):
    dist = [INF] * (N + 1)
    q = []
    heapq.heappush(q, (start, 0))

    while q:
        ci, cd = heapq.heappop(q)

        # ci까지 가는 저장된 비용보다 cd가 더 크다면 의미 없으므로 continue.
        if dist[ci] < cd:
            continue

        # 더 적은 비용을 발견한 경우, 연결된 ci의 인접 노드로의 최소 비용을 다시 계산.
        for ni, nd in edge[ci]:
            if dist[ni] > cd + nd:
                dist[ni] = cd + nd
                heapq.heappush(q, (ni, cd + nd))
    
    # start 노드에서 다른 모든 노드까지의 최소 비용을 저장한 리스트를 리턴.
    return dist


if __name__ == "__main__":
    N, E = map(int, input().split())
    graph = [[] for _ in range(N + 1)]

    for _ in range(E):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    # stop_over(경유지) 1, 2    
    stov1, stov2 = map(int, input().split())

    path_all = dijkstra(1, graph)           # 1에서 모든 노드로의 최단 경로
    path_stov1 = dijkstra(stov1, graph)      # 경유지 1에서 모든 노드로의 최단 경로
    path_stov2 = dijkstra(stov2, graph)      # 경유지 2에서 모든 노드로의 최단 경로
    
    # v1 == 1 && v2 == N 인 반례 때문에 82% 컷.
    if 1 != stov1 and stov2 != N:
        way1 = path_all[stov1] + path_stov1[stov2] + path_stov2[N]      # 1 -> 경유지1 -> 경유지 2 -> N
        way2 = path_all[stov2] + path_stov2[stov1] + path_stov1[N]      # 1 -> 경유지2 -> 경유지 1 -> N
    else:
        way1 = way2 = path_all[N]
    
    # 경로가 없을 경우 -1 출력 조건을 깜빡했더니 75% 컷.
    print(min(way1, way2) if way1 < INF or way2 < INF else -1)