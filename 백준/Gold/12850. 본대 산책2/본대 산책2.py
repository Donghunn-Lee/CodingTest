# 본대 산책2

# 인접 행렬을 알지 못하면 풀 수 없는 문제였음.
# 물론 내가 알 턱이 없기에 풀지 못함.
# i * j 형태의 행렬을 N제곱했을 때 i에서 j로 가는 경우의 수가 곧 i행j열의 값.
# 인접 행렬에 대해 이해하고 있었다면, 행렬의 곱과 거듭제곱만으로 풀 수 있었던 문제.
# 수학은 너무 어려웡 그래서 인접행렬이 먼데 => 그래프에서 N개의 정점 간 간선 존재 유무를 표시한 N차 행렬.

import sys
input = sys.stdin.readline
MOD =  1_000_000_007
SIZE = 8

# 행렬 곱
def mul_matrix(a, b):
    result = [[0] * SIZE for i in range(SIZE)]

    for i in range(SIZE):
        for j in range(SIZE):
            for k in range(SIZE):
                result[i][j] += a[i][k] * b[k][j]
            result[i][j] %= MOD
    
    return result

# 거듭제곱
def power(a, n):
    if n == 1:
        return a
    
    tmp = power(a, n // 2)

    if n % 2 == 0:
        return mul_matrix(tmp, tmp)
    else:
        return mul_matrix(mul_matrix(tmp, tmp), a)

if __name__ == "__main__":
    D = int(input())

    # i에서 j로 가는 이동시간.
    matrix = [
        [0, 1, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 0, 0, 0, 0],
        [1, 1, 0, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 1, 0, 0],
        [0, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 0, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 0, 1, 0]
    ]

    ans = power(matrix, D)
    print(ans[0][0])