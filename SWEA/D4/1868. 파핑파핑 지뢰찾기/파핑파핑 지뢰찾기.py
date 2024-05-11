# 파핑파핑 지뢰찾기

from collections import deque

def check_zero(si, sj):
    deq = deque()
    deq.append((si, sj))
    is_zero = False

    while deq:
        tmp = []
        ci, cj = deq.popleft()

        for di, dj in near_side:
            ni, nj = ci + di, cj + dj

            if 0 <= ni < N and 0 <= nj < N:
                tmp.append((ni, nj))

                if graph[ni][nj] == '*':
                    tmp = []
                    break
        
        if tmp:
            is_zero = True

            for ti, tj in tmp:
                if not visited[ti][tj]:
                    visited[ti][tj] = 1
                    deq.append((ti, tj))

            visited[ci][cj] = 1

    return is_zero


if __name__ == "__main__":
    T = int(input())
    ans = []

    near_side = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i != 0 or j != 0:
                near_side.append((i, j))


    for t in range(1, T + 1):
        N = int(input())
        graph = [list(input().rstrip()) for _ in range(N)]
        visited = [[0] * N for _ in range(N)]
        empty_space = 0
        zeros = 0

        for i in range(N):
            for j in range(N):
                if graph[i][j] == '.':
                    empty_space += 1

                    if not visited[i][j] and check_zero(i, j):
                        zeros += 1
        
        checked = sum(list(map(sum, visited[:])))

        ans.append(f'#{t} {empty_space - checked + zeros}')

    print("\n".join(ans))