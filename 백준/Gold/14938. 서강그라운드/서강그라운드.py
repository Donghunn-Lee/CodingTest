import sys
INF = int(1e9)
n, m, r = map(int, input().split())

items = [0] + [int(x) for x in sys.stdin.readline().split()]

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(r):
    a, b, l = map(int, sys.stdin.readline().split())
    graph[a][b] = l
    graph[b][a] = l

for i in range(n + 1):
    graph[i][i] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

ans = 0
for i in range(1, n + 1):
    tmp = 0
    for j in range(1, n + 1):
        if graph[i][j] <= m:
            tmp += items[j]

    ans = max(ans, tmp)

print(ans)