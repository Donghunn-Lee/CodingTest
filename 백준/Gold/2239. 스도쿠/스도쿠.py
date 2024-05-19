# 스도쿠

# 그냥 스도쿠에서 뭔가 다른 variation은 없어서 크게 어렵진 않았음.
# 0인 좌표를 뽑아 dfs로 각 좌표에 모든 값을 대입해보고, 이 때 규칙상 중복이 아닌지 체크하고 dfs를 다시 실행함.
# 시간은 pypy로 5000ms가 넘게 나옴. 그래서 내가 잘못 푼 건가? 하고 찾아보니 대부분 크게 다르지 않게 풀었음.
# 다만 획기적으로 빠른 방법이 있었는데, 바로 비트마스킹.
# 스도쿠 역시 9*9의 행렬에 1~9의 수가 채워져 있는 것이다 보니 비트마스킹으로 수의 존재 여부를 확인할 수 있었음.
# 지금은 말고 다음에 스도쿠 관련 문제를 풀게 되면 그 때는 비트마스킹을 사용해 보는 걸로?
# 3시간 뒤 싸피 코테인데 진짜 잘 봤으면 좋겠다.

import sys
input = sys.stdin.readline

# 소속된 정방형 칸과 가로, 세로에 지금 넣으려는 수가 있는지를 확인.
def check(i, j, n):
    pi, pj = i // 3 * 3, j // 3 * 3
    
    for ci in range(pi, pi + 3):
        for cj in range(pj, pj + 3):
            if graph[ci][cj] == n:
                return False
    
    for cur in range(9):
        if graph[cur][j] == n or graph[i][cur] == n:
            return False
    
    return True

# dfs로 구해놓은 좌표들을 순회하며 가능한 모든 수를 대입.
def dfs(cur):
    global complete

    # 종료를 위해 조건을 지키면서 모든 수를 채웠을 때, complete를 True로 변경.
    # 사전식으로 앞서는 경우를 출력해야하기 때문에 처음 정답을 발견 후 더 탐색할 필요가 없음.
    if cur == zero_count:
        complete = True
        return
    
    # 이미 정답을 찾았으면 종료.
    if complete:
        return

    ci, cj = zeros[cur]

    for n in range(1, 10):
        if check(ci, cj, n):
            graph[ci][cj] = n
            dfs(cur + 1)

            # 정답을 찾아서 종료된 이후에 다시 값을 되돌리지 않도록 종료 조건을 이 곳에도 추가.
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
    
    dfs(0)

    for i in graph:
        ans.append(''.join(map(str, i)))
    
    print("\n".join(ans))