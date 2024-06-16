# 가장 긴 증가하는 부분 수열 2

# 이분 탐색으로 bisect 모듈을 사용하면 간단한 문제. 하지만 혼자서는 못 품.
# 다만 이렇게 구한 LIS는 내용까지 LIS 인 것은 아니고, 길이만 구하는 문제이기에 풀 수 있음.

import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
A = [*map(int, input().split())]

LIS = [A[0]]

for item in A:
    if LIS[-1] < item:
        LIS.append(item)
    else:
        idx = bisect_left(LIS, item)
        LIS[idx] = item

print(len(LIS))