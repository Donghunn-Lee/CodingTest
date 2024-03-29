# 트리의 지름

# dfs 자체는 어렵지 않은데 양 끝점을 어떻게 찾아야 할지 한참 고민한 문제.
# 30분만에 dfs는 작성했는데, 끝점을 찾기 위해 정렬도 해보고 이것 저것 해보며 2시간이나 날림. 그냥 빨리 답 찾아볼걸
# 고로 찾아본 풀이는 트리의 성질을 이용한 것.
# 임의의 노드에서 가장 멀리 있는 노드는 반드시 트리의 지름 양 끝점 중 하나이다. 왜 이런 생각을 못했을까.
# 고로 아무 노드에서나 1회 dfs를 돌려서 하나의 끝점을 찾아내고, 그 점을 시작으로 다시 한 번 dfs를 돌리면 해결되는 문제.

# +++ 난 dfs로 풀었는데 왜 또 다들 bfs로 푼 걸까. 이런 문제에서 어떤 점이 bfs가 더 효율적이라고 판단되는 기준인지 아직도 잘 모르겠음.
import sys
input = sys.stdin.readline

# first와 그냥의 차이는 코드 내 edge의 유무.
def dfs_first(graph, visited, start, distance):
    global max_dis
    global edge
    
    if max_dis < distance:
        edge = start
        max_dis = distance

    for k in graph[start].keys():
        if not visited[k]:
            visited[k] = True
            dfs_first(graph, visited, k, distance + graph[start][k])


def dfs(graph, visited, start, distance):
    global max_dis

    if max_dis < distance:
        max_dis = distance

    for k in graph[start].keys():
        if not visited[k]:
            visited[k] = True
            dfs(graph, visited, k, distance + graph[start][k])


if __name__ == "__main__":
    V = int(input())
    graph = [{} for i in range(V + 1)]
    visited = [False] * (V + 1)
    max_dis, edge = 0, 0

    for i in range(V):
        n, *info = map(int, input().split())
        for j in range(0, len(info) - 1, 2):
            graph[n][info[j]] = info[j + 1]
    
    # 양 끝점 중 하나 찾기
    visited = [False] * (V + 1)
    visited[1] = True
    dfs_first(graph, visited, 1, 0)

    # 찾은 점에서 최대 거리 계산
    visited = [False] * (V + 1)
    visited[edge] = True
    dfs(graph, visited, edge, 0)

    print(max_dis)
