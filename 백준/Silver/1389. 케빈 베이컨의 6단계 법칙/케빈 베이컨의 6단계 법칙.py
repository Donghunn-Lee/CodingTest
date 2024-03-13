# 케빈 베이컨의 6단계 법칙

# 쉬워보였는데 순서를 더하는 방법을 생각하지 못해서 꽤 오랜 시간을 들인 문제.
# 최단 거리를 구하는 것이나 마찬가지니 bfs가 적합하다고 생각했으나
# 연결된 정점들의 순서, 즉 거리를 더하는 방법을 고민해도 생각해내지 못해서 우선 dfs로 풀었다가 시간초과.
# 이후 검색을 통해 거리 리스트를 만들고, 현재 정점의 거리에 1을 더하는 방식이 있다는 것을 깨달았음.
# 그렇게 하면 최초 발견한 정점은 1일 때, 큐에서 꺼낸 방문했던 정점에서 찾은 노드는 현 정점의 거리 + 1이 됨.
import sys
from collections import deque
input = sys.stdin.readline

def bfs(rel, s):
    kevin_bacon = [0] * (N + 1)
    visited = [False] * (N + 1)
    q = deque()
    q.append(s)

    while q:
        cur = q.popleft()   # 그동안 쓰면서 생각 못했는데 pop(0)은 처음부터 끝까지 찾아가므로 O(n)이고
                            # popleft()는 처음에서 바로 꺼내므로 O(1)임.
        for i in rel[cur]:
            if not visited[i]:
                # 여기서 새로 발견한 정점의 거리를 현재 정점의 거리 + 1로 할당.
                kevin_bacon[i] = kevin_bacon[cur] + 1
                visited[i] = True
                q.append(i)
    
    return sum(kevin_bacon)

if __name__ == "__main__":

    N, M = map(int, input().split())
    relationship = [[] for _ in range(N + 1)]
    ans = []

    for _ in range(M):
        a, b = map(int, input().split())
        relationship[a].append(b)
        relationship[b].append(a)

    for i in range(1, N + 1):
        ans.append(bfs(relationship, i))
    
    print(ans.index(min(ans)) + 1)