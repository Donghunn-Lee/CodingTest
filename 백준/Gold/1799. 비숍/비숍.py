# 비숍

# 퀸을 찾는 문제가 비숍을 찾는 문제로 바뀜.
# 그런데 대각선으로 하니까 인덱스를 어떻게 굴려야 할 지 고민이 돼서 어려웠음.

# 검색해보니 dfs가 기본으로 하고, 우상향과 우하향 대각선을 체크해가며 비숍을 두는 방식.
# 퀸이 같은 행과 열에 하나밖에 존재할 수 없다는 것을 이용해 row 리스트만 생성했던 것처럼, 비숍의 대각선 리스트 생성.
# 이후 각 대각선마다 놓을 수 있는 곳에 비숍을 두고, 그 자리를 고려해 다시 다음 대각선에서 놓을 수 있는 곳에 비숍을 둠.
# 매번 반복시 upper_bound로 현재 대각선 이후의 대각선들 중 대각선 내 한 곳이라도 둘 수 있는 곳을 세어서 반환,
# 그 값과 cnt의 합이 현재 갱신된 ans보다 작으면 종료하는 방식으로 가지치기.

# +++ 핵심은 비숍은 우상향 대각선에 하나만 존재할 수 있고, 해당 칸이 포함된 우하향 대각선에도 하나만 존재해야함.
# 우상향 대각선확인은 재귀함수 인자로 입력받기에 2 * N - 1개의 대각선을 각 함수에서 하나씩 탐색함.
# 우하향 대각선은 placed 딕셔너리를 사용해 1과 0으로 유무를 확인함.
import sys
input = sys.stdin.readline

# 입력받은 대각선 이후의 놓을 수 있는 자리가 있는 대각선의 수를 반환.
def upper_bound(diag):
    placeable = 0

    for d in range(diag, 2 * N - 1):
        for i in range(d + 1):
            j = d - i

            # 대각선 검사시 비숍을 놓을 수 있는 칸인지를 확인.
            if 0 <= i < N and 0 <= j < N and board[i][j] and placed[j - i] == 0:
                placeable += 1
                break
    
    return placeable

# 백트래킹을 통해 비숍을 가장 많이 놓을 수 있는 방법을 계산.
def backtracking(diag, cnt):
    global ans

    # 모든 대각선을 확인한 경우 종료.
    if diag == 2 * N - 1:
        ans = max(ans, cnt)
    
    ub = upper_bound(diag)

    # 더 계산해봤자 ans를 높일 수 없는 경우에 종료함으로써 가지치기.
    if ub + cnt <= ans:
        return
    
    # 우상향 대각선을 기준으로 0부터 2 * N - 2 번 대각선까지 탐색.
    for i in range(diag + 1):
        j = diag - i

        if 0 <= i < N and 0 <= j < N and board[i][j] and placed[j - i] == 0:
            # 놓을 수 잇는 자리라면 우하향 대각선에 체크.
            placed[j - i] = 1

            backtracking(diag + 1, cnt + 1)
            
            # 해당 지점에 놓은 경우를 모두 탐색 후, 백트래킹을 위해 초기화.
            placed[j - i] = 0
    
    backtracking(diag + 1, cnt)

if __name__ == "__main__":
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    placed = {i : 0 for i in range(-N + 1, N)}
    ans = 0

    backtracking(0, 0)
    print(ans)