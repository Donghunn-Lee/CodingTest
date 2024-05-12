# 문제집

# 두 번째 위상 정렬 문제.
# 처음엔 graph를 저장하고 1부터 연결된 노드들을 저장, 가장 큰 노드를 다른 리스트에 넣고 낮은 것부터 출력했음.
# 그러나 3번을 풀기 쉽게 하는 조건이 1번과 2번 이렇게 두 가지 있는 경우를 계산할 수 없었음.

# 분류를 확인하니, 전에 한 번 풀어본 적 있는 위상 정렬 문제.
# 순서가 있는 간선이 주어진다? 위상 정렬을 바로 떠올릴 수 있어야 함.
# 진입 차수가 0인 노드 리스트를 만들고 진입 차수를 계산해서 저장.
# 각 노드와 연결된 간선을 하나씩 꺼내어 진입 차수 차감.
# 진입 차수가 0인 경우엔 해당 노드를 큐에 넣어 위 과정을 반복.
import sys, heapq
input = sys.stdin.readline

def topology_sort():
    q = []

    # 진입 차수가 0인 노드를 힙에 입력.
    for i in range(1, N + 1): 
        if in_degree[i] == 0:
            heapq.heappush(q, i)

    # 진입 차수를 차감하고 0인 경우 큐에 다시 넣기를 반복.
    while q:
        cur = heapq.heappop(q)

        # 큐에서 꺼낸 노드는 진입 차수가 0인 것으로 해당 문제에선 이미 푼 문제로 취급, ans에 저장.
        ans.append(cur)

        for i in edges[cur]:
            in_degree[i] -= 1

            if in_degree[i] == 0:
                heapq.heappush(q, i)


if __name__ == "__main__":
    N, M = map(int, input().split())
    edges = [[] for _ in range(N + 1)]
    in_degree = [0 for _ in range(N + 1)]
    ans = []

    # 간선을 입력받으며 진입 차수를 갱신.
    for i in range(M):
        a, b = map(int, input().split())
        edges[a].append(b)
        in_degree[b] += 1
    
    topology_sort()

    print(" ".join(map(str, ans)))