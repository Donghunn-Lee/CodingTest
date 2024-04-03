# 최소비용 구하기

# 그냥 평범한 다익스트라 문제.
# 단방향 엣지가 주어지고, 시작점과 도착점이 주어지고 최소 비용을 출력하는 일반적인 유형.
import sys, heapq
input = sys.stdin.readline
INF = 1e10

def dijkstra(graph, s, dest, n):
    min_cost = [INF] * (n + 1)
    q = []
    heapq.heappush(q, (0, s))

    while q:
        cur_cost, cur = heapq.heappop(q)

        if min_cost[cur] < cur_cost:
            continue

        # 목적지가 주어지는 경우, 음수 간선이 없는 이상 현재 노드가 목적지일 때의 반복은 의미가 없으므로 패스.
        if cur == dest:
            break
        
        for nxt_cost, nxt in graph[cur]:
            nxt_cost += cur_cost
            if min_cost[nxt] > nxt_cost:
                min_cost[nxt] = nxt_cost
                heapq.heappush(q, (nxt_cost, nxt))
    
    return min_cost[dest]


if __name__ == "__main__":
    N = int(input())
    M = int(input())
    graph = [[] for _ in range(N + 1)]
    
    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[a].append((c, b))     # 시간 효율을 위해 (거리, 정점) 순으로 튜플 저장.
    
    start, dest = map(int, input().split())

    print(dijkstra(graph, start, dest, N))