# 알파벳

# bfs를 쓰려다가 문득 조건에 따라 방향을 바꿔 움직이는 건 dfs라는 것을 떠올려 dfs를 사용.
# 그리고 예제1처럼 같은 문자가 2개 이상 인접해 있는 경우, 한 쪽을 선택해 방문 표시를 하고 나면 다른 쪽은 못 가므로
# 백트래킹까지 해줘야겠다고 생각함. 입력 수가 20*20으로 현저히 적은 것에서도 추측함.

# +++ 재귀 dfs로 풀긴 했으나, 7800ms. 재귀 방식 자체도 문제고 방문 체크도 문제인 것 같아서 검색후 다른 코드를 참고.
# visited의 각 좌표에 방문한 문자들을 순서대로 넣어서, 그 길이로 ans를 초기화.
# 그리고 visited에 저장된 문자를 비교해서 방문 여부를 확인.
# bfs에선 popleft를 쓰지만, dfs
import sys
input = sys.stdin.readline

def dfs(si, sj, alpha):
    stack = [(si, sj, alpha)]
    visited = [[''] * C for _ in range(R)]
    dir = ((1, 0), (0, 1), (-1, 0), (0, -1))
    ans = 0

    visited[si][sj] = alpha
    
    while stack:
        ci, cj, alpha = stack.pop()

        if ans < len(alpha):
            ans = len(alpha)
        
        if ans == 26:
            return ans

        for d in dir:
            ni, nj = ci + d[0], cj + d[1]

            if 0 <= ni < R and 0 <= nj < C and graph[ni][nj] not in alpha:
                nxt_alpha = alpha + graph[ni][nj]

                if visited[ni][nj] != nxt_alpha:
                    visited[ni][nj] = nxt_alpha
                    stack.append((ni, nj, nxt_alpha))
    
    return ans

if __name__ == "__main__":
    R, C = map(int, input().split())
    graph = [list(input().rstrip()) for _ in range(R)]

    print(dfs(0, 0, graph[0][0]))