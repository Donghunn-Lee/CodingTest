# 트리와 쿼리

# 문제가 길고 무슨 말인지 이해가 안 가서 한참 쳐다만 봄.
# 여기서 쿼리의 의미와 처음 주어진 트리가 루트가 있는 트리라는 점을 제대로 파악해야 함.
# 결국 구해야 하는 건 루트 있는 트리에서 임의의 정점이 가진 자식 노드의 수였음.
# 이걸 먼저 알았다면 풀었을 것 같은데, 검색해서 코드를 보면서 깨달았기 때문에 혼자서는 못 품.

# 우선 모든 정점에 대한 서브트리의 수를 계산.
# dfs로 루트를 기준하여 모든 정점을 탐색.
# 트리에서 한 정점을 두 번 방문하는 경우는 없으므로 방문체크. => 곧 서브트리 개수가 됨.
# 그 다음은 주어진 쿼리에 해당하는 visited 값을 출력하기만 하면 끗.
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(n):
    visited[n] = 1

    for i in tree[n]:
        if not visited[i]:
            dfs(i)
            visited[n] += visited[i]


if __name__ == "__main__":
    N, R, Q = map(int, input().split())
    tree = [[] for _ in range(N + 1)]
    visited = [0] * (N + 1)
    ans = []

    for _ in range(N - 1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
    
    dfs(R)

    query = [int(input()) for _ in range(Q)]

    for i in query:
        ans.append(visited[i])
    
    print("\n".join(map(str, ans)))