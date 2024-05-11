# 도시 분할 계획

# 사이클을 떠올려놓고 최소 스패닝 트리를 떠올리지 못함. 음수 사이클이 발생하면 이를 확인하는 벨만포드를 떠올림.
# 떠올리기만 하고 아닌 것 같아서 끙끙대다 분류를 확인하고 최소 스패닝 트리임을 깨달았음.
# 구현 잘 기억나지 않아서 검색. 보니까 좀 기억이 나지만 이전에도 완벽하게 이해는 못했던 게 생각남. 이번에도 역시.

# 핵심 원리는 최소 스패닝 트리에서 하나의 간선을 제거하면 그 산물은 두 개의 스패닝 트리임을 이용.
# 문제만 읽고는 잘 이해가 안 됐는데, 그렇게 생각하니 문제의 의도가 바로 이거구나 하고 이마를 탁! 치게 되었음.
# 아무튼 간선이 엄청 많을 때(기준은 모르겠고)는 프림 알고리즘이고, 보통은 크루스칼 알고리즘으로 최소 스패닝 트리 도출.
# 그리고 정렬했으므로 최소 스패닝 트리에 마지막으로 들어가는 간선이 가장 높은 비용이므로 이를 뺀 결과값을 출력.

import sys
input = sys.stdin.readline

# find. 전엔 몰랐는데 이게 union-find 알고리즘의 그 find 인 것 같음.
# 입력받은 노드의 루트를 찾아 올라가서 현재 루트 노드를 리턴.
def find_parant(x):
    if parent[x] != x:
        parent[x] = find_parant(parent[x])
    
    return parent[x]

# 이것 역시 union-find의 그 union.
# find로 구한 값을 parent에 갱신. 더 하위 노드 인덱스 값에 상위 노드를 갱신.
# 최소 스패닝 트리가 완성되면 parent가 [1, 1, 1...]로 완성됨.
def union_parant(a, b):
    if a < b:
        parent[b] = a

    else:
        parent[a] = b

# 비용으로 오름차순 정렬한 간선들을 모두 탐색하여 parent에 union-find.
def kruskal(edges):
    result = 0
    bigest_cost = 0

    for a, b, c in edges:
        a, b = find_parant(a), find_parant(b)
        if a != b:
            union_parant(a, b)
            result += c

            # 오름차순 정렬이므로 마지막에 저장되는 값이 가장 큰 비용의 간선이 됨.
            # 해당 간선을 제거하고 스패닝 트리를 2개로 만드는 것.
            bigest_cost = c
    
    return result - bigest_cost

if __name__ == "__main__":
    N, M = map(int, input().split())
    parent = [i for i in range(N + 1)]
    edges = []

    for _ in range(M):
        edges.append(list(map(int, input().split())))
    edges.sort(key = lambda x : x[2])

    print(kruskal(edges))