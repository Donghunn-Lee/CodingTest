# 체스판 다시 칠하기

# 실 4인데 의외로 머리를 좀 써야 했던 문제. 일단 문제 이해도 잘 안 됐음.
# 요는 8*8의 윈도우를 전체 보드 위에서 움직이며 그 안에서 체스판이 아닌 최소 칸 수를 계산. 일종의 슬라이딩 윈도우?

import sys
input = sys.stdin.readline

def like_chess():
    ans = 1e9

    for i in range(N - 7):
        for j in range(M - 7):
            cnt_1, cnt_2 = 0, 0

            for ni in range(i, i + 8):
                for nj in range(j, j + 8):
                    if (ni + nj) % 2 == 0:
                        if board[ni][nj] != 'B':
                            cnt_1 += 1
                        if board[ni][nj] != 'W':
                            cnt_2 += 1

                    else:
                        if board[ni][nj] != 'W':
                            cnt_1 += 1
                        if board[ni][nj] != 'B':
                            cnt_2 += 1

            ans = min(ans, cnt_1, cnt_2)
    
    return ans

if __name__ == "__main__":
    N, M = map(int, input().split())
    board = [input().rstrip() for _ in range(N)]
    
    print(like_chess())
