# 미로 1

from collections import deque

def bfs(si, sj):
    deq = deque()
    deq.append((si, sj))
    visited = [[0] * 16 for _ in range(16)]
    dir = ((0, 1), (1, 0), (-1, 0), (0, -1))

    while deq:
        ci, cj = deq.popleft()

        for di, dj in dir:
            ni, nj = ci + di, cj + dj

            if 1 <= ni < 15 and 1 <= nj < 15 and not visited[ni][nj]:
                if graph[ni][nj] == '0':
                    deq.append((ni, nj))
                    visited[ni][nj] = 1
                
                elif graph[ni][nj] == '3':
                    return 1

    return 0

if __name__ == "__main__":
    ans = []

    for t in range(1, 11):
        T = int(input())
        graph = [list(input().rstrip()) for _ in range(16)]

        ans.append(f'#{t} {bfs(1, 1)}')
    
    print("\n".join(ans))