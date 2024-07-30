from collections import deque

def bfs(si, sj, visited, N, M, land, group) :
    visited[si][sj] = 1
    
    deq = deque()
    deq.append((si, sj))
    visited_j = set()
    visited_j.add(sj)
    count = 1
    
    while deq:
        ci, cj = deq.popleft()
        
        for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            ni, nj = ci + di, cj + dj
            
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                if land[ni][nj] == 1:
                    deq.append((ni, nj))
                    visited[ni][nj] = 1
                    visited_j.add(nj)
                    count += 1
    
    for i in visited_j:
        group[i] += count 
                    
    

def solution(land):
    N, M = len(land), len(land[0])
    group = [0] * M
    visited = [[0] * M for _ in range(N)]
        
    for i in range(N):
        for j in range(M):
            if land[i][j] == 1 and not visited[i][j]:
                bfs(i, j, visited, N, M, land, group)
            
    return max(group)

print(solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]))