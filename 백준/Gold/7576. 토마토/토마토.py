# 토마토 standard

# 골드 5짜리라 빠르게 풀어버리려고 했는데, 방향성을 잘못 잡아서 생각보다 오래 걸렸음.첫트는 시간초과.
# 먼저 익은 토마토를 찾고 deq에 추가.
# 인접한 덜 익은 토마토를 ripening에 추가.
# deq을 ripeing으로 덮어씌워주고, 다음 날을 탐색.
# 처음에 익을 수 있는 토마토의 개수를 세고, 이후 새롭게 토마토가 익을 때 차감시켜서 0이면 모든 토마토가 익음.

import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    deq = deque()
    visited = [[0] * M for _ in range(N)]
    num_tomato, date = 0, 0

    # 먼저 익은 토마토의 위치와 덜 익은 토마토의 수를 파악.
    for i in range(N):
        for j in range(M):
            if tomatos[i][j] == 0:
                num_tomato += 1

            if tomatos[i][j] == 1:
                deq.append((i, j))

    # 반복
    while deq:
        ripening = deque()
        
        while deq:
            ci, cj = deq.popleft()

            for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                ni, nj = ci + di, cj + dj

                if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                    # 익은 토마토인 현재 지점에서 인접한 덜 익은 토마토를 발견한 경우,
                    # ripeing에 추가 후 방문 체크.
                    if tomatos[ni][nj] == 0:
                        ripening.append((ni, nj))
                        visited[ni][nj] = 1
        
        # 새로 익을 토마토가 있다면 deq을 초기화하고 num_tomato를 차감.
        # 날짜도 추가.
        if ripening:
            deq = ripening
            num_tomato -= len(ripening)
            date += 1
        
        # 없다면 더 이상 탐색할 수 없음.
        else:

            # 덜 익은 토마토의 수가 0이면 모든 토마토가 익은 것이므로 date를 반환.
            if num_tomato == 0:
                return date
            
            # 아닌 경우엔 -1을 반환.
            else:
                return -1
    
    # 처음부터 익은 토마토가 하나도 없어서 deq이 비어있을 경우, -1 을 반환.
    return -1


if __name__ == "__main__":
    M, N = map(int, input().split())
    tomatos = [list(map(int, input().split())) for _ in range(N)]

    print(bfs())