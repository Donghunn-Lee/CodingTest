# 소수 찾기

import sys
input = sys.stdin.readline

N = int(input())

nums = list(map(int, input().rstrip().split()))
ans = 0

def findPrimeNumber(n):
    count = 0
    i = 1
    while i <= n:
        if count > 2:
            return 0
        if n % i == 0:
            count += 1
        i += 1
    if count == 2:
        return 1
    else:
        return 0

for i in range(N):
    ans += findPrimeNumber(nums[i])

print(ans)