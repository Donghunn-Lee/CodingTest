# 2048 (Easy)
import copy, sys
input = sys.stdin.readline
# dfs로 모든 방향의 경우를 완전탐색해야 하는 문제
# 각각의 방향에 따라 2중 for문 내 변수위치를 다르게 해야 하기 때문에 각각 함수 구성

def push_right(board):
    for i in range(N):
        cur = N - 1 # 시작지점에 커서 표시
        for j in range(N - 2, -1, -1):  # 밀려는 방향의 끝에서 시작
            if board[i][j]:
                # tmp 에 현재 값을 저장, 현재 값에는 우선 0을 저장
                tmp, board[i][j] = board[i][j], 0   
            
                # 현재 값이 들어있는 tmp와 커서가 가리키는 값이 같다면 병합
                # 한 번 합쳐진 값은 그 턴에 더 합쳐질 수 없으므로 커서 이동
                if board[i][cur] == tmp:
                    board[i][cur] *= 2
                    cur -= 1
                
                # 0인 경우 현재 값을 커서 위치로 이동.
                elif board[i][cur] == 0:
                    board[i][cur] = tmp

                # 커서 값이 현재 값과 다르고 0이 아닌 경우 커서를 이동
                # 이 경우는 이동한 위치가 현재 위치거나 다른 수가 합쳐져 커서가 0인 경우밖에 없음
                else:
                    cur -= 1
                    board[i][cur] = tmp
                    
    return board


# 다른 방향 함수의 경우엔 for문의 i와 j, 범위, 커서 증감 방향을 목적에 맞게 변경
def push_left(board):
    for i in range(N):
        cur = 0
        for j in range(1, N):
            if board[i][j]:
                tmp, board[i][j] = board[i][j], 0
            
                if board[i][cur] == tmp:
                    board[i][cur] *= 2
                    cur += 1
                elif board[i][cur] == 0:
                    board[i][cur] = tmp
                else:
                    cur += 1
                    board[i][cur] = tmp
                    
    return board
            
def push_up(board):
    for j in range(N):
        cur = 0
        for i in range(1, N):
            if board[i][j]:
                tmp, board[i][j] = board[i][j], 0
            
                if board[cur][j] == tmp:
                    board[cur][j] *= 2
                    cur += 1
                elif board[cur][j] == 0:
                    board[cur][j] = tmp
                else:
                    cur += 1
                    board[cur][j] = tmp
                    
    return board
            
def push_down(board):
    for j in range(N):
        cur = N - 1
        for i in range(N - 2, -1, -1):
            if board[i][j]:
                tmp, board[i][j] = board[i][j], 0
            
                if board[cur][j] == tmp:
                    board[cur][j] *= 2
                    cur -= 1
                elif board[cur][j] == 0:
                    board[cur][j] = tmp
                else:
                    cur -= 1
                    board[cur][j] = tmp
                    
    return board

# dfs로 완전탐색. 입력된 기회를 모두 사용하면 전역변수 max_num에 현 루트의 보드 최댓값을 저장하고 종료.
def dfs(board, cnt):
    global max_num

    if cnt == 0 :
        max_num = max(max_num, max(map(max, board)))
        return
    
    # for문에 함수를 넣어 모든 방향을 탐색
    for f in push_left, push_right, push_up, push_down:
        tmp_board = copy.deepcopy(board)
        dfs(f(tmp_board), cnt - 1)

if __name__ == "__main__":
    max_num = 0
    N = int(input())
    tzfe = [list(map(int, input().split())) for _ in range(N)]

    dfs(tzfe, 5)

    print(max_num)
