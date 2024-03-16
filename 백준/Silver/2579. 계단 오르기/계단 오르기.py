# 계단 오르기

# dp 점화식 문제는 몇 개 기억 나는 게 있는데도 이번 문제는 또 다른 방식이라 어려웠음.
# 전에 푼 점화식 문제들은 맨 끝 인덱스에서 조금씩 줄어들었다면, 이번엔 더해가는것이 맞는 방법.
# 뒤에서도 풀 수 있나 확인은 해봐야겠음.

import sys
input = sys.stdin.readline

# 한 번에 -3 까지 확인하므로 dp역시 3까지 미리 생성.
# i번째 계단에 갈 수 있는 두 방법 중 더 큰 값을 선택해 더해가며 반복하는 방식.
def climb(s, n):
    # 계단이 1개나 2개 주어지는 경우도 있어서 아래 조건 추가.
    if n == 1:
        return s[1]
    if n == 2:
        return s[1] + s[2]
    
    dp = {1 : s[1], 2 : s[1] + s[2], 3 : max(s[1] + s[3], s[2] + s[3])}
            
    for i in range(4, n + 1):
        dp[i] = max(dp[i - 3] + s[i - 1] + s[i], dp[i - 2] + s[i])

    return dp[n]

if __name__  == "__main__":
    N = int(input())
    stairs = [0] + [int(input()) for _ in range(N)]
    
    print(climb(stairs, N))