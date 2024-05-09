# 격자판의 숫자 이어 붙이기

def dfs(ci, cj, cur, length):
    if length == 7:
        visited.add(cur)
        return
    
    for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        ni, nj = ci + di, cj + dj

        if 0 <= ni < 4 and 0 <= nj < 4:
            dfs(ni, nj, cur + str(graph[ni][nj]), length + 1)

if __name__ == "__main__":
    T = int(input())
    ans = []

    for t in range(1, T + 1):
        graph = [list(map(int, input().split())) for _ in range(4)]
        visited = set()

        for i in range(4):
            for j in range(4):
                dfs(i, j, str(graph[i][j]), 1)
        
        ans.append(f'#{t} {len(visited)}')
    
    print("\n".join(ans))