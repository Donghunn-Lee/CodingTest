# 행성 터널

# 5티어라지만 플레문제인데 검색 없이 내가 전에 푼 코드만 다시 좀 참고해서 풀어냈
# 다고 생각했었지만 역시 플레문제였음. 최소 스패닝 트리 알고리즘으로 푸는 것은 맞는 듯한데, 간선 계산에서 메모리 초과.
# 행성이 100,000개나 있을 수 있으니 생각은 했지만 중간에 잊음.
# 크루스칼은 떠올린 다음 내가 전에 푼 코드에서 참고할 수 있었고, 핵심이 되는 간선 계산 부분은 결국 검색해서 참고함.

# 간선을 가지치기 하는 방법은, 행성 간 이동 비용은 x, y, z 축 간 거리 중 가장 작은 값이므로, 각 축 별로 리스트를 분리.
# 분리한 x, y, z 좌표값 리스트를 정렬. 이 때 행성 정보를 알 수 있게 튜플에 행성 번호를 미리 추가함.
# 모든 행성은 가장 가까운 행성이 하나씩 있고, 최소 스패닝 트리에 사용되는 간선은 두 행성을 잇는 최소 비용의 간선.
# 이를 이용해 각각 오름차순 정렬한 세 리스트를 기반으로, 순서대로 간선을 추가함.

# 정리하자면 최소 스패닝 트리, 크루스칼 알고리즘을 사용해 풀어야 하는 문제.
# 간선이 아닌 정점의 정보가 3차원으로 주어짐. 간선을 만들어야 함.
# 간선을 만들기 위해 3차원 정보를 각각의 1차원 정보로 만들고, 그 정렬된 일직선상에서 순서대로 두 점을 잇는 간선을 추가.
# 크루스칼 알고리즘은 가중치가 작은 간선부터 탐색하므로, 정렬을 해도 되지만 간선 수가 적지 않으므로 애초에 heap을 사용.
import sys, heapq
input = sys.stdin.readline

def cal_distance(a, b):
    x1, y1, z1 = planets[a]
    x2, y2, z2 = planets[b]

    return min(abs(x1 - x2), abs(y1 - y2), abs(z1 - z2))

def find(x):
    if x != root[x]:
        root[x] = find(root[x])

    return root[x]

def kruskal():
    cnt, min_weight = 0, 0

    while cnt < N - 1:
        w, a, b = heapq.heappop(edges)
        a_root, b_root = find(a), find(b)

        # 더 작은 수가 부모가 됨.
        if a_root != b_root:
            if a_root < b_root:
                root[b_root] = a_root
            
            else:
                root[a_root] = b_root

            min_weight += w
            cnt += 1

    return min_weight

if __name__ == "__main__":
    N = int(input())
    planets = [list(map(int, input().split())) + [i] for i in range(N)]
    root = [i for i in range(N)]

    x_sort = sorted(planets, key = lambda x : x[0])
    y_sort = sorted(planets, key = lambda x : x[1])
    z_sort = sorted(planets, key = lambda x : x[2])
    edges = []
    for i in range(N - 1):
        heapq.heappush(edges, (abs(x_sort[i][0] - x_sort[i + 1][0]), x_sort[i][3], x_sort[i + 1][3]))
        heapq.heappush(edges, (abs(y_sort[i][1] - y_sort[i + 1][1]), y_sort[i][3], y_sort[i + 1][3]))
        heapq.heappush(edges, (abs(z_sort[i][2] - z_sort[i + 1][2]), z_sort[i][3], z_sort[i + 1][3]))

    print(kruskal())