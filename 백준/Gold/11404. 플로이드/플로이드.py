# 플로이드

# 플로이드-워셜 문제를 풀어 본 적이 없으니 당연히 다익스트라 문제라고 생각, 풀었는데 풀렸음.
# 아마 방식 자체가 다익스트라를 n번 더 돌리는 느낌인 것 같아서 시간복잡도상 큰 차이가 나지 않는 듯함.
# 아무튼 다익스트라로 맞췄지만 문제 이름부터 플루이드니까 검색해서 다시 풀어봄.
# 플로이드-워셜 알고리즘은 모든 노드에서 다른 모든 노드로 가는 최소 비용을 다차원 리스트에 저장함.
# 다익스트라보다도 더 단순한 코드. 핵심인 점화식 자체도 어렵진 않음.

import sys, heapq
input = sys.stdin.readline
INF = 1e10

def floyd_warshall(graph):
    result = []

    # 자기 자신을 0으로 초기화.
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                graph[i][j] = 0

    # 점화식. i에서 j로 갈 때 k노드를 거쳐서 가는 것과 바로 가는 것을 비교하며 최소 비용 갱신.
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1 , n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    # 계산 후 갈 수 있는 경우의 수가 없는 경우 0으로 초기화.
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][j] == INF:
                graph[i][j] = 0

        result.append(" ".join(map(str, graph[i][1:])))
    
    return "\n".join(result)


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    ans = []

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a][b] = min(c, graph[a][b])
    
    print(floyd_warshall(graph))
    