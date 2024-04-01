# 최단경로

# 최근 다익스트라를 자주 접해서 그런지 이제 코드 구성 자체는 외운 듯. 하지만 아직도 힙을 쓰는 이유 등은 모르겠음.
# 우선 풀었던 문제들보다도 단순함. 그냥 단방향 엣지, 특정 노드에서 모든 노드로의 최단 경로를 구하면 되는 문제.
import sys, heapq
input = sys.stdin.readline
INF = 1e10

def dijkstra(s):
    dist = [INF] * (V + 1)
    dist[K] = 0     # 시작노드를 0 초기화 해주는 것이 중요. 다시 돌아오는 간선이 존재하기 때문.
    q = []

    # 최소 힙에서 튜플의 대소비교는 원소 순서.
    #  정점이 아니라 거리를 0번 인덱스로 써야 함. 아니면 시간초과.
    heapq.heappush(q, (0, s))

    while q:
        cd, ci = heapq.heappop(q)

        if dist[ci] < cd:
            continue

        for ni, nd in graph[ci]:
            if dist[ni] > cd + nd:
                dist[ni] = cd + nd
                heapq.heappush(q, (cd + nd, ni))
    
    return dist

if __name__ == "__main__":
    V, E = map(int, input().split())
    K = int(input())
    graph = [[] for _ in range(V + 1)]
    # ans = []
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))

    path = dijkstra(K)

    for i in range(1, V + 1):
        if path[i] == INF:
            print("INF")
            continue

        print(path[i])

    # print("\n".join(ans))