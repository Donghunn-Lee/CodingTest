# 단지번호붙이기

import sys
from collections import deque
input = sys.stdin.readline

# 전형적인 bfs 문제에 반복 구간이 추가된 케이스.
# 전체 좌표를 돌며 1이 인접한 구간을 찾아 n에 그 구간의 1의 수를 더함.
# 구간에 더이상 인접한 1이 없어서 while문이 종료된 경우 n을 count에 추가.
# visited는 구간별로 초기화 하지 않고 전제 좌표를 다시 돌아 방문하지 않은 1 발견시 다시 while문 진입.
# 이를 반복하여 여러 개의 구간과 각 구간의 1의 개수를 계산하여 반환.
def bfs(ap):
    q = deque()
    
    dir = ((0, 1),(1, 0), (-1, 0), (0, -1))
    visited = []
    ap_c = [] # 아파트 단지와 아파트 수를 저장하는 변수.
    
    # 전체 좌표를 돌며 방문하지 않은 1을 탐색, 발견하면 비어있는 덱에 해당 좌표를 추가.
    for i in range(N):
        for j in range(N):
            if (i, j) not in visited and ap[i][j] == '1':
                q.append((i, j))
                visited.append((i, j))
                n = 1   # 1을 찾은 시점에서 상하좌우 탐색을 시작하므로 1로 시작.

                while q:
                    ci, cj = q.popleft()
                    for d in dir:
                        ni, nj = ci + d[0], cj + d[1]
                        if 0 <= ni < N and 0 <= nj < N and (ni, nj) not in visited:
                            if ap[ni][nj] == '1':
                                q.append((ni, nj))
                                n += 1  #발견시 덱에 추가함과 동시에 n += 1.
                            visited.append((ni, nj))
                # while 종료 == 해당 구간 탐색 끝이므로 n을 ap_c에 추가.
                ap_c.append(n)
    
    if ap_c:
        ap_c.sort()
        return f"{len(ap_c)}\n"+'\n'.join(map(str, ap_c))
    else:
        return 0

if __name__ == "__main__":
    N = int(input())
    apartment_complexes = [list(input().rstrip()) for _ in range(N)]
    
    print(bfs(apartment_complexes))