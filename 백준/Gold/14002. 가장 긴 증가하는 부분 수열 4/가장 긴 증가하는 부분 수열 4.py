# 가장 긴 증가하는 부분 수열

N = int(input())

A = list(map(int, input().split()))
dp = [1] * N
ans = []

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)

seq = []
lenA = max(dp)

for i in range(1, N + 1):
    if dp[-i] == lenA:
        seq.insert(0, A[-i])
        lenA -= 1
            

for i in seq:
    ans.append(str(i))

print(len(ans))
print(' '.join(ans))