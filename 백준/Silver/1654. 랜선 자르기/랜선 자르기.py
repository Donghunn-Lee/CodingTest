# 랜선 자르기

import sys
input = sys.stdin.readline

def max_cable():
    max_length = 0
    left, right = 0, max(seq) + 1

    while left + 1 < right:

        length = left + (right - left) // 2
        cnt = 0
        
        for i in seq:
            cnt += i // length

        if N <= cnt:
            left = length
            max_length = max(max_length, length)
        
        else:
            right = length


    return max_length


if __name__ == "__main__":
    K, N = map(int, input().split())
    seq = [int(input()) for _ in range(K)]
    
    print(max_cable())