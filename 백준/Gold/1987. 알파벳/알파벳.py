# 알파벳

# bfs를 쓰려다가 문득 조건에 따라 방향을 바꿔 움직이는 건 dfs라는 것을 떠올려 dfs를 사용.
# 그리고 예제1처럼 같은 문자가 2개 이상 인접해 있는 경우, 한 쪽을 선택해 방문 표시를 하고 나면 다른 쪽은 못 가므로
# 백트래킹까지 해줘야겠다고 생각함. 입력 수가 20*20으로 현저히 적은 것에서도 추측함.
# 방문한 좌표가 아니라 문자가 기준이므로, 이동가능한 최대 칸 수를 저장할 리스트와 방문한 문자 리스트를 각각 생성.

import sys
input = sys.stdin.readline

def dfs(ci, cj, dist):
    # 함수 실행 시 visited_alpha에 문자 추가.
    visited_alpha.add(graph[ci][cj])
    
    # 현재 좌표에 이동해온 거리를 할당.
    visited_dist[ci][cj] = max(visited_dist[ci][cj], dist)

    for d in dir:
        ni, nj = ci + d[0], cj + d[1]
        if 0 <= ni < R and 0 <= nj < C and graph[ni][nj] not in visited_alpha:
            # 인덱스 내에서 이동하며, dist + 1.
            dfs(ni, nj, dist + 1)
    
    # 함수에서 입력받은 좌표에서 갈 수 있는 방향을 모두 확인했다면 백트래킹을 위해 제거.
    visited_alpha.remove(graph[ci][cj])
    

if __name__ == "__main__":
    R, C = map(int, input().split())
    graph = [list(input().rstrip()) for _ in range(R)]
    visited_alpha = set()
    visited_dist = [[0] * C for _ in range(R)]
    dir = ((1, 0), (0, 1), (-1, 0), (0, -1))

    dfs(0, 0, 1)

    print(max(map(max, visited_dist)))