# 외판원 순회

# 물론 혼자선 전혀 방법을 떠올릴 수 없었음. 그냥 다 돌리면 무조건 시간초과가 나 버리니.

# 이번 문제는 난 처음 들어보지만 꽤 유명한 듯. Traveling Salesman problem, TSP라고 불리는 문제.
# dp와 비트 마스킹을 활용해야 시간과 공간 복잡도를 줄여 풀어낼 수 있었음.
# 비트가 들어가면 일단 매우 어려워짐. 그래도 이 문제는 이해하려고 하면 할 수는 있는 문제였음. 참고한 해설이 친절했기도.

# 핵심은 

import sys
input = sys.stdin.readline

def dfs(cur, visited):
    # 모든 도시를 방문한 경우 종료.
    if visited == (1 << N) - 1:

        # 이 때 출발했던 도시로 다시 돌아올 수 있는지를 확인.
        # 0번 도시를 사용해도 괜찮은 이유는, 같은 경로에서라면 어떤 도시에서 출발하든 전체 비용은 동일하기 때문.
        if graph[cur][0]:
            return graph[cur][0]
        
        # 아닌 경우 무한대를 반환.
        else:
            return int(1e9)
    
    # 이미 구한 경로인 경우 저장된 dp 테이블 값을 반환.
    if (cur, visited) in dp:
        return dp[(cur, visited)]
    

    min_cost = int(1e9)

    # 모든 도시를 방문하며 dfs 탐색.
    for nxt in range(1, N):

        # 비용이 0(갈 수 없는 경로)이거나 이미 방문한 도시인 경우, continue.
        # 비트의 & 연산의 경우, 비트중 겹치는 부분이 하나도 없어야 0이 됌.
        if graph[cur][nxt] == 0 or visited & (1 << nxt):
            continue

        # 갈 수 있는 경우, 지금 방문한 도시를 출발점으로 하고 visited에 추가한 상태로 다음 도시를 탐색.
        cost = dfs(nxt, visited | (1 << nxt)) + graph[cur][nxt]
        min_cost = min(min_cost, cost)

    dp[(cur, visited)] = min_cost

    return min_cost

if __name__ == "__main__":
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    dp = {}

    print(dfs(0, 1))