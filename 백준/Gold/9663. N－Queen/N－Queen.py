# N-Queen

# 쉬워보였는데 어려웠던 문제.
# 당연히 체스판을 표현한 이차원 리스트를 사용했었음.
# 그리고 퀸을 놓으면 그 공격 범위를 전부 체크하는 방식을 썼지만 어림도 없음.
# 결국 해법을 찾아보니 길이 n짜리 리스트 하나로 체크를 할 수 있었음. 퀸은 행과 열당 하나밖에 못 두니까.
# 그리고 대각선 좌표 사이의 규칙, 같은 대각선상이면 행-열의 값이 같다는 점일 이용해 대각선도 체크.
# 확실히 아직도 한참 문제를 더 풀어봐야 하겠다는 생각을 계속 하게 됌.

import sys
input = sys.stdin.readline

def is_safe(ci):
    for j in range(ci):
        if row[ci] == row[j] or abs(row[ci] - row[j]) == abs(ci - j):
            return False
    
    return True

def put_the_queen(i):
    global ans
    if i == N:
        ans += 1
        return

    for j in range(N):
        row[i] = j
        if is_safe(i):
            put_the_queen(i + 1)

if __name__ == "__main__":
    N = int(input())
    row = [0] * N
    ans = 0

    put_the_queen(0)
    print(ans)