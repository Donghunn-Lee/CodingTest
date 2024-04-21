# 최소비용 구하기 2

# 처음엔 q에 거리와 노드하나가 아니라 지나온 노드를 담은 리스트를 추가해서 반복하려고 함.
# 그렇게 하니 50%에서 틀리는데 여전히 이유는 정확히 모르겠음. n_cost를 비교하는 부분에서 <를 <=로 바꾸니 메모리 초과.

# 다른 방법을 찾다가 부모 관계의 리스트를 하나 만들어서 특정 노드(인덱스)의 상위 노드(값)을 저장하는 방법을 알게 됌.
# parant가 초기화되는 경우는 더 낮은 코스트가 갱신될 때이므로, 마지막에 남은 값이 각 노드로의 최소 비용 간선임.
# 다 풀고 보니 그냥 min_cost에 나는 노드가 담긴 리스트를 넣었었는데 그 자리에 그냥 상위 노드값만 넣으면 됐었네?
# 라고 여길수도 있겠지만 나는 a에서 b로 가는 최소 비용을 찾는 다익스트라 안에서 만들어서 추가만 할 줄 알았지 상위 노드를 갱신한다는 생각을 하지 못함.

# +++ 메모리 초과 원인... 보통 다익스트라를 풀 땐 INF = 1e10을 기본으로 넣고 해왔음.
# 다만 이번 문제에는 비용의 최댓값이 100000이라는 문구가 눈에 들어와서 100000으로 최소 비용 리스트를 초기화 함.
# 아무리 봐도 알고리즘은 잘못된 게 없는데 계속해서 메모리 초과가 났던 이유가 여기에 있었음.
# 돌아보며 여타 풀이와 내 풀이에 다른 게 한계치 설정밖에 없는 것 같아 INF = 1e10을 넣고 돌려보니 통과.
# 이후 검색해서 변수명의 메모리를 확인하는 sys.getsizeof()로 확인해보니 100000 은 28바이트, 1e10은 24바이트.
# 이 사소한 차이로 메모리 초과가 날 줄은 전혀 예상하지 못했음. n이 1000이여도 4kb차이인데 사실 아직도 이해가 잘 안 됌.

import sys, heapq
input = sys.stdin.readline
INF = 1e10

def dijkstra(start):
    q = []
    q.append((0, start))
    
    while q:
        cost, cur = heapq.heappop(q)

        if min_cost[cur] < cost:
            continue

        for n_cost, nxt in graph[cur]:
            n_cost += cost
            if min_cost[nxt] > n_cost:
                min_cost[nxt] = n_cost
                # nxt노드로 가는 가장 적은 비용을 가진 노드로써 cur이 저장.
                parant[nxt] = cur
                heapq.heappush(q, (n_cost, nxt))



if __name__ == "__main__":
    n = int(input())
    m = int(input())
    parant = [i for i in range(0, n + 1)]
    graph = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((c, b))

    start, target = map(int, input().split())

    min_cost = [INF] * (n + 1)
    min_cost[start] = 0
    passed_by = [target]

    dijkstra(start)

    print(min_cost[target])
    
    # target 노드부터 해당 노드의 상위 노드로 저장된 노드를 갱신해가며 passed_by에 추가.
    while target != start:
        target = parant[target]
        passed_by.append(target)
    
    passed_by.reverse()

    
    print(len(passed_by))
    print(" ".join(map(str, passed_by)))
