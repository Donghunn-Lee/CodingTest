# 스도쿠

import sys
input = sys.stdin.readline

def check(i, j, n):
    pi, pj = i // 3, j // 3
    
    for ci in range(pi * 3, pi * 3 + 3):
        for cj in range(pj * 3, pj * 3 + 3):
            if graph[ci][cj] == n:
                return False
    
    for cur in range(9):
        if graph[cur][j] == n or graph[i][cur] == n:
            return False
    
    return True

def dfs(cur, count):
    global complete

    if count == zero_count:
        complete = True
        return
    
    ci, cj = zeros[cur]

    for n in range(1, 10):
        if check(ci, cj, n):
            graph[ci][cj] = n
            dfs(cur + 1, count + 1)

            if complete:
                return
            
            graph[ci][cj] = 0


if __name__ == "__main__":
    graph = [list(map(int, list(input().rstrip()))) for _ in range(9)]
    ans = []

    zeros = []
    zero_count = 0
    for i in range(9):
        for j in range(9):
            if graph[i][j] == 0:
                zeros.append((i, j))
                zero_count += 1

    complete = False
    
    dfs(0, 0)

    for i in graph:
        ans.append(''.join(map(str, i)))
    
    print("\n".join(ans))