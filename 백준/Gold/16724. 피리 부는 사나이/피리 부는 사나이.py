# 피리 부는 사나이

# 최근 골드 문제들에도 조금 쫄긴 했는데, 이 문제는 그래프 문제라서 그런지 크게 어렵지 않았음.
# SAFE ZONE 설치의 요는 그래프 내에서 발생한 사이클과 관련 있다는 것.
# 멈추지 못하고 계속 반복된다는 것은 사이클이 존재한다는 것이며, 그 사이클을 끊는 지점이 SAFE ZONE.
# 따라서 dfs로 모든 지점에서 발생할 수 있는 사이클을 찾고, 그 사이클의 수가 곧 SAFE ZONE의 수가 됨.
import sys
input = sys.stdin.readline

def dfs(i, j):
    global safe_zone

    # 방문 여부와 현재 탐색중인 사이클 갱신.
    visited[i][j] = 1
    cycle.add((i, j))

    # 방향에 따른 이동. if문이 길어져 딕셔너리를 생성함.
    di, dj = dir[graph[i][j]]
    ni, nj = i + di, j + dj

    # 방문하지 않은 곳이면 계속해서 dfs 실행.
    if not visited[ni][nj]:
        dfs(ni, nj)
    
    # 방문했던 곳이며 현재 사이클에 들어있는 지점이라면 사이클이 발생했으므로 safe_zone + 1.
    # 이때 방문했으면서 현재 사이클이 없다면, 이전에 탐색한 사이클에 진입하는 것이므로 세지 않음.
    elif (ni, nj) in cycle:
        safe_zone += 1


if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = [input().rstrip() for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    dir = {'U' : (-1, 0), 'D' : (1, 0), 'L' : (0, -1), 'R' : (0, 1)}
    safe_zone = 0

    for i in range(N):
        for j in range(M):
            cycle = set()
            dfs(i, j)

    print(safe_zone)