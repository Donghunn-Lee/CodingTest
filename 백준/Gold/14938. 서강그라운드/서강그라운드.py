import heapq
import sys
INF = int(1e9)
n, m, r = map(int, input().split())

items = [0] + [int(x) for x in sys.stdin.readline().split()]

graph = [[] for _ in range(n + 1)]

for _ in range(r):
    a, b, l = map(int, sys.stdin.readline().split())
    graph[a].append([b, l])
    graph[b].append([a, l])

def dijkstra(start):
    que = []
    heapq.heappush(que, (0, start))
    D[start] = 0

    while que:
        dist, now = heapq.heappop(que)
        if D[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < D[i[0]]:
                D[i[0]] = cost
                heapq.heappush(que, (cost, i[0]))

ans = 0
for i in range(1, n + 1):
    D = [INF] * (n + 1)
    dijkstra(i)
    tmp = 0
    for d in range(1, n + 1):
        if m >= D[d]:
            tmp += items[d]

    ans = max(ans, tmp)

print(ans)