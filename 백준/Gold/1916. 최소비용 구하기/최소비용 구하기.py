# 최소비용 구하기

# 그냥 평범한 다익스트라 문제.
# 단방향 엣지가 주어지고, 시작점과 도착점이 주어지고 최소 비용을 출력하는 일반적인 유형.
import sys, heapq
input = sys.stdin.readline
INF = 1e10

def dijkstra(s):
    min_cost = [INF] * (N + 1)
    q = []
    heapq.heappush(q, (0, s))

    while q:
        cur_cost, cur = heapq.heappop(q)

        if min_cost[cur] < cur_cost:
            continue

        for nxt_cost, nxt in graph[cur]:
            tmp = nxt_cost + cur_cost
            if min_cost[nxt] > tmp:
                min_cost[nxt] = tmp
                heapq.heappush(q, (tmp, nxt))
    
    return min_cost


if __name__ == "__main__":
    N = int(input())
    M = int(input())
    graph = [[] for _ in range(N + 1)]
    
    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[a].append((c, b))     # 시간 효율을 위해 (거리, 정점) 순으로 튜플 저장.
    
    start, dest = map(int, input().split())

    print(dijkstra(start)[dest])