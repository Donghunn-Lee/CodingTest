# LCS 2

# 꽤 전에 풀었던 LCS와 거의 동일하지만, 이번엔 길이만이 아니라 그 값도 구하는 문제.
# 직전 문제가 냅색 알고리즘이었는데 이 문제도 2차원 dp테이블을 사용해서 조금 이해가 빨랐음.
# 고비는 같은 문자를 찾았을 때, 어느 것을 기준으로 현재 dp를 갱신해야 하는지에 대한 부분. 여기서 좀 헤맸음.
# 그 점만 이해하면 나머지는 쉬웠음. 길이 대신 문자열을 저장하는 것으로 문자열을 구해낼 수 있음.

import sys
input = sys.stdin.readline

def LCS2(a, b):
    dp = [[''] * len(b) for _ in range(len(a))]

    for i in range(1, len(a)):
        for j in range(1, len(b)):
            if a[i] == b[j]:
                dp[i][j] = dp[i - 1][j - 1] + b[j]
            
            else:
                # 가능한 lcs중 아무거나 출력하면 되므로, 길이가 같은 경우엔 어느쪽이든 상관 없음. 나는 j - 1을 사용.
                if len(dp[i][j - 1]) < len(dp[i - 1][j]):
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i][j - 1]

    return dp[-1][-1]

if __name__ == "__main__":
    A = ' ' + input().rstrip()
    B = ' ' + input().rstrip()

    result = LCS2(A, B)
    
    print(len(result))
    
    if result:
        print(result)
    