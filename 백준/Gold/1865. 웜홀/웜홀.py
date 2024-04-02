# 웜홀

# 당연히 다익스트라인줄 알고 풀었는데, 29% 시간초과.
# 음수 루프의 존재는 처음부터 생각하고, 시작 노드의 값이 0보다 작아지면 리턴하도록 했는데 부족했음.
# 잠시 고민하다가 혹시나 싶어 알고리즘 분류를 확인해보니 다익스트라가 아닌 '벨만-포드 알고리즘'
# 엊그제 처음 본 다익스트라처럼 벨만포드도 오늘 처음 봤으므로 검색해서 짧은 강의로 이해한 뒤 코드 작성.
# 다익스트라가 시작 노드에서 인접한 노드로의 간선을 찾는다면, 벨만포드는 모든 간선을 매번 탐색해서 음수 순환 감지 가능.
import sys, heapq
input = sys.stdin.readline
INF = 1e10

def bf():
    for i in range(N):
        for j in range(len(graph)):
            ci, ni, cost = graph[j]

            # 노드에 저장된 시간보다 더 짧아질 경우 초기화.
            if time[ni] > time[ci] + cost:
                time[ni] = time[ci] + cost

            # 0부터 N - 2까지 반복되는 동안, 1번 정점부터 N - 1번 정점이 모두 N번 정점과 비교 한 셈.
            # 때문에 마지막 반복 시에도 위 조건이 참이 되어 time이 초기화 될 경우, 음수 순환이 존재함.
                if i == N - 1:
                    return True

    return False

if __name__ == "__main__":
    TC = int(input())
    ans = []

    for _ in range(TC):
        N, M, W = map(int, input().split())
        graph = []
        time = [INF] * (N + 1)

        for _ in range(M):
            S, E, T = map(int, input().split())
            graph.append((S, E, T))
            graph.append((E, S, T))

        for _ in range(W):
            S, E, T = map(int, input().split())
            graph.append((S, E, -T))
        
        if bf():
            ans.append('YES')
        else:
            ans.append('NO')
    
    print("\n".join(ans))