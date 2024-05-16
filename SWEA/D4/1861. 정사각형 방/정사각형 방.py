# 정사각형 방

# 전형적인 bfs/dfs 문제. 뭐가 더 효율적인지는 잘 모르겠음.
# 시작하는 방부터 1로 치는 걸 몰라서 5분 더 걸림.
# 매 방마다 딱 1씩 더 큰 방으로 이동할 수 있기 때문에 visited가 필요 없었음.
# 모든 좌표에서 bfs를 돌리고, 이동 횟수를 리턴. 최대치를 저장해가며 같은 경우 더 작은 방 번호로 갱신함.

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

