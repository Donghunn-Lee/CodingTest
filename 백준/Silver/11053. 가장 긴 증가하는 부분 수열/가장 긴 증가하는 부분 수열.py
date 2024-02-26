# 가장 긴 증가하는 부분 수열

N = int(input())

A = list(map(int, input().split()))
d = [1] * N

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            d[i] = max(d[i], d[j] + 1)

print(max(d))