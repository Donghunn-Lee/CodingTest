# 연속합

N = int(input())
candys = [list(input().rstrip()) for _ in range(N)]
result = 0
visited = set()

# 입력된 좌표를 행과 열의 연속된 사탕 수의 최댓값을 리턴
def counting(ci, cj):
    count, tmpH, tmpV = 1, 1, 1
    for i in range(N - 1):

        # 가로 방향
        if candys[ci][i] == candys[ci][i + 1]:
            tmpH += 1
        elif candys[ci][i] != candys[ci][i + 1]:
            count = max(count, tmpH)
            tmpH = 1
        
        # 세로 방향
        if candys[i][cj] == candys[i + 1][cj]:
            tmpV += 1
        elif candys[i][cj] != candys[i + 1][cj]:
            count = max(count, tmpV)
            tmpV = 1

    return max(count, tmpH, tmpV)

# 좌상단을 원점으로 우측과 하단 각 1칸씩을 교환하며 counting 함수 실행
# counting 함수의 리턴 값 중 최댓값을 저장하여 리턴
def bfs():
    count_max = 1
    for i in range(N):
        for j in range(N):
            if j + 1 < N and candys[i][j] != candys[i][j + 1]:
                candys[i][j], candys[i][j + 1] = candys[i][j + 1], candys[i][j]
                count_max = max(count_max, counting(i, j), counting(i, j + 1))      # 현재 위치와 +1 한 위치 각각에서 가로세로 탐색
                candys[i][j], candys[i][j + 1] = candys[i][j + 1], candys[i][j]

            if j + 1 == N:      # j의 끝에서 왼쪽과 교환하여 체크
                candys[i][j], candys[i][j - 1] = candys[i][j - 1], candys[i][j]
                count_max = max(count_max, counting(i, j))
                candys[i][j], candys[i][j - 1] = candys[i][j - 1], candys[i][j]

            if i + 1 < N and candys[i][j] != candys[i + 1][j]:
                candys[i][j], candys[i + 1][j] = candys[i + 1][j], candys[i][j]
                count_max = max(count_max, counting(i, j), counting(i + 1, j))      # 현재 위치와 +1 한 위치 각각에서 가로세로 탐색
                candys[i][j], candys[i + 1][j] = candys[i + 1][j], candys[i][j]

            if i + 1 == N:  # i의 끝에서 위쪽과 교환하여 체크
                candys[i][j], candys[i - 1][j] = candys[i - 1][j], candys[i][j]
                count_max = max(count_max, counting(i, j))
                candys[i][j], candys[i - 1][j] = candys[i - 1][j], candys[i][j]

    return count_max

# 바꾸지 않아도 이미 최대값이 존재할 경우를 대비해 최초 1회 전체 탐색
for i in range(N):    
    result = max(result, counting(i, i)) # counting은 가로와 세로를 동시에 탐색하므로 좌하단 방향으로의 대각선만 고려하면 됨.

result = max(result, bfs())
print(bfs())