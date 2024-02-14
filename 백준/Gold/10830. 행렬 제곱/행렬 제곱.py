# 행렬 제곱
import sys
input = sys.stdin.readline

N, B = map(int, input().split())
mat_A = [list(map(int, input().split())) for _ in range(N)]
C = 1000

def mul_matrix (m1, m2) :
    result = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += m1[i][k] * m2[k][j] % C
    return result

def DC (mat, p) :
    if p == 1:
        return mat
    else:
        tmp = DC(mat, p // 2)

        if p % 2:
            return mul_matrix(mul_matrix(tmp, tmp), mat)
        else:
            return mul_matrix(tmp, tmp)

result = DC(mat_A, B)

for row in result:
    for col in row:
        print(col % C , end=" ")
    print()