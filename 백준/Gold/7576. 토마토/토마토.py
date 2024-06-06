# 토마토 standard

# 골드 5짜리 엄청 빠릴 풀어버리려고 했는데 30분이나 잡아먹음. 단순 bfs가 아니라 약간 더 뭐가 있긴 했음.
# bfs로 풀려고 했는데 뭔가 bfs라기엔 조금 아쉬운 느낌? 결이 조금 다른 느낌을 받았음.

import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    deq = deque()
    visited = [[0] * M for _ in range(N)]
    num_tomato, date = 0, 0

    for i in range(N):
        for j in range(M):
            if tomatos[i][j] == 0:
                num_tomato += 1

            if tomatos[i][j] == 1:
                deq.append((i, j))

    while deq:
        ripening = deque()
        
        while deq:
            ci, cj = deq.popleft()

            for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                ni, nj = ci + di, cj + dj

                if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                    if tomatos[ni][nj] == 0:
                        ripening.append((ni, nj))
                        visited[ni][nj] = 1
        
        if ripening:
            deq = ripening
            num_tomato -= len(ripening)
            date += 1
        
        else:
            if num_tomato == 0:
                return date
            
            else:
                return -1
    
    return -1


if __name__ == "__main__":
    M, N = map(int, input().split())
    tomatos = [list(map(int, input().split())) for _ in range(N)]

    print(bfs())

    
