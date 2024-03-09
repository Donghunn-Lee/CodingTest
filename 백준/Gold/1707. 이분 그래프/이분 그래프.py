# 이분 그래프

import sys
sys.setrecursionlimit(10**6)    # 파이썬 기본 재귀 제한이 1000으로 매우 낮아 재귀 제한 확장 필수.
input = sys.stdin.readline

# dfs를 활용하고 그룹을 나누는 것 가진 혼자 생각할 수 있었음.
# 다만 함수 종료조건을 설정하고 함수를 반복을 제어할 방법을 생각하지 못했음.
def DFS(edges, visited, start, group):
    visited[start] = group  # visited에 그룹 지정.

    # start 지점과 연결된 인접 노드를 탐색.
    for i in edges[start]:
        if not visited[i]:  # 방문하지 않은 노드인 경우 이를 start로 DFS에 그룹을 바꿔서 입력.
            result = DFS(edges, visited, i, -group)
            # 앞선 함수에서 False를 반환받은 경우, 재귀를 종료해야 하므로 다시금 False를 반환.
            if not result:
                return False
        else:
            # 방문한 노드인 경우에는
            # 현재 함수 스코프의 start 노드가 속한 그룹과 일치여부를 검사.
            # 일치시 이분 그래프가 아니므로 False를 반환.
            if visited[i] == group:
                return False

    # 모두 False를 반환받지 못한 경우엔 이분 그래프이므로 True를 반환.
    return True


if __name__ == "__main__":
    K = int(input())
    
    for _ in range(K):
        V, E = map(int, input().split())
        edges = [[] for _ in range(V + 1)]
        visited = [False] * (V + 1)
        
        for i in range(E):
            u, v = map(int, input().split())
            edges[u].append(v)
            edges[v].append(u)
        
        for i in range(1, V + 1):
            # 다른 DFS 문제와 다르게, 방문 후 함수 종료시 다시 visited를 초기화 하지 않음.
            # 이유는 DFS가 True를 반환했다는 것은 모든 노드를 방문해서 이분 그래프임을 확인했다는 의미임.
            # 따라서 함수를 다른 시작점에서 재실행할 필요가 없음. 문제만 이해하면 단순한 이유임.
            if not visited[i]:
                ans = DFS(edges, visited, i, 1)
                
                # False를 반환받은 경우 반복 종료.
                if not ans:
                    break
        
        print("YES") if ans else print("NO")