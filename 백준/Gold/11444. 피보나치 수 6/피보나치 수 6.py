# 피보나치 수 6

## 분할 정복을 이용한 거듭제곱

# 수학 문제는 역시 너무 어려움. 그래도 조금 더 보려고 했으면 규칙을 찾을 법도 했는데, 빠르게 포기.
# 사실 이 방법이 아닌 다른 방법이 더 정석처럼 보이는데, 이해가 쉽지 않음.
# 우선 단순해보여서 참고한 아래 방법은 n번째 수가 홀수이고 짝수일 때의 규칙을 활용한 분할정복.


import sys
input = sys.stdin.readline

def fibonacci(n):
    if dp.get(n):
        return dp[n]
    
    if n == 0:
        return 0
    
    if n == 1 or n == 2:
        return 1
    
    # 짝수라면 n // 2를 기준으로 앞 뒤 수를 빼면 n번째 수열 값이 나옴.
    if n % 2 == 0:
        dp[n // 2 + 1] = fibonacci(n // 2 + 1)
        dp[n // 2 - 1] = fibonacci(n // 2 - 1)
        return (dp[n // 2 + 1] ** 2 - dp[n // 2 - 1] ** 2) % 1_000_000_007
    
    # 홀수일 땐 n // 2를 기준으로 해당 수와 +1번째 수를 더함.
    else:
        dp[n // 2 + 1] = fibonacci(n // 2 + 1)
        dp[n // 2] = fibonacci(n // 2)
        return (dp[n // 2 + 1] ** 2 + dp[n // 2] ** 2) % 1_000_000_007
    
if __name__ == "__main__":
    N = int(input())
    dp = dict()

    print(fibonacci(N))