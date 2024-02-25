# 쉬운 계단 수

N = int(input())
stairs = [[0] * 10 for _ in range(N + 1)]

for i in range(1, 10):
    stairs[1][i] = 1

def DP(n):
    for i in range(2, n + 1):
        for j in range(10):
            if j == 9:
                stairs[i][j] = stairs[i - 1][j - 1]
            elif j == 0:
                stairs[i][j] = stairs[i - 1][j + 1]
            else:
                stairs[i][j] = stairs[i - 1][j + 1] + stairs[i - 1][j - 1]
    return sum(stairs[N]) % 1000000000

print(DP(N))