# 플로이드

# 다익스트라를 안 푼지 조금 되어서 떠올리느라 살짝 고민했던 문제.
# 아마 저번주에 풀었다면 20분만에 풀었을 문제. 어려운 건 전혀 없었음.
# 모든 노드의 쌍에 대해 최솟값을 구해야 하므로, 모든 노드에 대해 최소 비용을 구하면 됌.

import sys, heapq
input = sys.stdin.readline
INF = 1e10

def djikstra(edges):
    result = []

    for i in range(1, n + 1):
        dist = [INF] * (n + 1)
        q = []
        heapq.heappush(q, (0, i))

        while q:
            cost, cur = heapq.heappop(q)

            if dist[cur] < cost:
                continue

            for nxt_cost, nxt in edges[cur]:
                tmp = cost + nxt_cost
                if dist[nxt] > tmp:
                    dist[nxt] = tmp
                    heapq.heappush(q, (tmp, nxt))

        dist[i] = 0

        # 도착하는 경우의 수가 없어 값이 INF이면 0으로 초기화.
        for j in range(1, n + 1):
            if dist[j] == INF:
                dist[j] = 0

        result.append(dist)

    return result


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    edges = [[] for _ in range(n + 1)]
    ans = []

    for _ in range(m):
        a, b, c = map(int, input().split())
        edges[a].append((c, b))

    result_list = djikstra(edges)

    for s in result_list:
        ans.append(" ".join(map(str, s[1:])))
    
    print("\n".join(ans))