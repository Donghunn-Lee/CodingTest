# 최소 스패닝 트리

# 암만 봐도 그냥 다익스트라나 음수 간선이 있다고 벨만 포듣 아닌 것 같았기에 바로 분류 확인.
# 최소 스패닝 트리 라고 아예 분류가 있었음. 크루스칼 알고리즘과 프림 알고리즘이 대표적.
# 최소 스패닝 트리 = 최소 신장트리 => 사이클이 존재하지 않고 모든 노드를 연결하는 그래프.
# 크루스칼은 간선을 정렬하므로 간선의 수가 적을 때 사용, 많으면 힙을 사용하는 프림.
# 우선 처음 보는 문제라 알고리즘을 거의 붙여넣었지만 일단 70%는 이해한 듯.
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
# root 노드를 찾아 갱신.
def find(n):
    if n != roots[n]:
        roots[n] = find(roots[n])
    
    return roots[n]

# 크루스칼 알고리즘. 
def kruskal():
    min_weight = 0

    # 간선의 start, end, weight를 꺼내어 사용.
    for s, e, w in edges:

        # 각 노드의 root를 find.
        s_root = find(s)
        e_root = find(e)

        # start와 end의 root가 서로 다른 경우 => 현재 간선이 사이클을 발생시키지 않는 경우.
        if s_root != e_root:

            # 현재 간선을 최소 스패닝 트리에 추가.
            # 더 작은 수가 부모가 됨.
            if s_root > e_root:
                roots[s_root] = e_root
            
            else:
                roots[e_root] = s_root

            # 간선이 추가된 경우 가중치를 더해서 갱신.
            min_weight += w

    return min_weight

if __name__ =="__main__":
    V, E = map(int, input().split())
    roots = [ i for i in range(V + 1)]
    edges = []

    for _ in range(E):
        edges.append(list(map(int, input().split())))

    # 가중치를 오름차순 정렬.
    # 정렬했기 때문에 가장 먼저 생성되는 스패닝 트리가 최소 스패닝 트리가 됌.
    edges.sort(key = lambda x : x[2])

    print(kruskal())