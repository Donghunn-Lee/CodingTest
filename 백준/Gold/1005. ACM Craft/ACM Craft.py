# ACM Craft

# target 번호에서부터 시작 번호로 가는 역순의 탐색으로 bfs를 사용해 값을 도출해서 통과인 줄 알았으나 메모리 초과.
# 이유는 간선이 많아졌을 때 그 모든 간선을 다 deq에 넣어서 메모리 초과가 발생하는 것.
# 방안이 없어서 알고리즘 분류를 확인해보니 '위상 정렬'이라는 아예 처음 보고 듣는 키워드가 있어서, 곧바로 검색해서 분석.

# 위상 정렬은 간선을 통과하는 데 순서 조건이 있을 때 사용할 수 있는 방법.
# 특정 노드로 진입하는 간선의 개수(이하 진입 차수)를 찾아 저장, 진입 차수 0인 노드를 시작 노드로 하여 탐색 시작.
# bfs형식의 탐색에서 시작 노드의 간선을 통해 다른 노드를 확인할 때, 앞서 구한 진입 차수를 차감.
# 진입 차수를 모두 차감하여 0이 되었을 때(해당 노드로 가는 조건이 만족된 경우) 다음 노드를 deq에 추가.
# 이상이 위상정렬의 기본이며, 해당 문제에선 건설이 완료되는 시간을 구하기 위해 dp를 만들어 매번 최대 시간을 갱신.
import sys
from collections import deque
input = sys.stdin.readline

# 위상 정렬
def topology_sort(w):
    deq = deque()
    dp = [0] * (N + 1)  # 각 노드로 가는 최대 시간(진입 조건 건물들이 모두 건설되는 시간)을 저장하는 dp테이블.

    # 진입 차수가 0인 노드를 시작점으로써 deq에 추가.
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            deq.append(i)
            dp[i] = time_taken[i]
    
    # 탐색 시작.
    while deq:
        cur = deq.popleft()

        # 현재 노드에서 이어진 노드를 확인.
        for nxt in graph[cur]:
            dp[nxt] = max(dp[nxt], dp[cur] + time_taken[nxt])   # nxt 건물까지 건설 완료되는 최대 시간을 갱신.

            # cur의 건물이 완성 된 것이니, 이를 선행 조건으로 하는 노드의 진입차수를 1 차감.
            # 1 이상인 경우, 그 개수만큼 다른 간선이 더 있으므로 나중에 현 nxt 노드를 다시 방문해서 확인하게 됨.
            in_degree[nxt] -= 1     

            # 진입 차수가 0인 경우 다음 건물의 건설을 시작할 수 있음. 고로 deq에 추가.
            if in_degree[nxt] == 0:
                deq.append(nxt)
    
    # w 번째 건물까지 모든 선행 조건을 만족하며 건설한 최단 시간을 갱신.
    return dp[w]


if __name__ == "__main__":
    T = int(input())
    ans = []

    for _ in range(T):
        N, K = map(int, input().split())
        time_taken = [0] + list(map(int, input().split()))
        graph = [[] for _ in range(N + 1)]
        in_degree = [0] * (N + 1)

        # graph를 입력받을 때 진입 차수의 수를 계산.
        for _ in range(K):
            a, b = map(int, input().split())
            graph[a].append(b)
            in_degree[b] += 1   
        
        W = int(input())

        ans.append(str(topology_sort(W)))
    
    print("\n".join(ans))