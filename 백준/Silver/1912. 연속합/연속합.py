# 연속합

import sys
input = sys.stdin.readline


def continuousSum(seq):
    max_sum = seq[0]
    current = 0

    # 0 이상의 수라면 current에 계속 더해서 한 묶음으로 만듦.
    # 만약 current가 음수가 된다면 앞의 연속합은 답이 아니므로 현재 n으로 초기화
    for n in seq:
        if current >= 0:
            current += n
        else:
            current = n
        if current > max_sum:
            max_sum = current
    return max_sum
    

if __name__ == "__main__":
    N = int(input())
    sequence = list(map(int, input().split()))

    print(continuousSum(sequence))