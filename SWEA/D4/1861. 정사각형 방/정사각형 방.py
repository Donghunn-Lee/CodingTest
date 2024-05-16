# 정사각형 방

from collections import deque

def bfs(si, sj):
    deq = deque()
    deq.append((si, sj, 1))
    moved = 0

    while deq:
        ci, cj, cnt = deq.popleft()

        if moved < cnt:
            moved = cnt

        for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ni, nj = ci + di, cj + dj

            if 0 <= ni < N and 0 <= nj < N:
                if graph[ni][nj] == graph[ci][cj] + 1:
                    deq.append((ni, nj, cnt + 1))
    
    return moved


if __name__ == "__main__":
    T = int(input())
    ans = []

    for t in range(1, T + 1):
        N = int(input())
        graph = [list(map(int, input().split())) for _ in range(N)]
        room_num, max_moved = 0, 0
        
        for i in range(N):
            for j in range(N):
                moved = bfs(i, j)
                
                if max_moved < moved:
                    room_num, max_moved = graph[i][j], moved

                elif max_moved == moved:
                    room_num = min(room_num, graph[i][j])
            
        ans.append(f'#{t} {room_num} {max_moved}')
    
    print("\n".join(ans))

