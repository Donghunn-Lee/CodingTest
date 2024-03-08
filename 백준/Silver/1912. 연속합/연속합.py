# 연속합
import sys
input = sys.stdin.readline


def continuousSum(seq):
    dp = []
    tmp = 0

    for i in seq:
        if i > 0:
            tmp += i
        else:
            if tmp:
                dp.append(tmp)
                tmp = 0
            dp.append(i)
    if not dp and tmp:
        dp.append(tmp)
    
    result = [dp[0]] + [0] * (len(dp)-1)

    for i in range(1, len(dp)):
        result[i] = max(dp[i], result[i-1] + dp[i])
        
    return max(result)
    

if __name__ == "__main__":
    N = int(input())
    sequence = list(map(int, input().split()))

    print(continuousSum(sequence))
