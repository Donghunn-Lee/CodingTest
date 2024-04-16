# 가장 긴 바이토닉 부분 수열

# 전에 가장 긴 부분 수열을 구하는 문제를 비슷한 걸로 두어 개 풀어 본 적이 있어서 개념은 어렵지 않게 떠올릴 수 있었음.
# 시간 복잡도는 정확이 어떻게 되는 지는 모르겠지만, O(N^2)에서 O(N*(N-i)) 식으로 계속해서 줄어드는 것 정도까지 이해함.

# 아무튼 이 문제를 풀기 위해선 앞에서부터 점점 증가하는 부분 수열을 구하고, 다시 뒤에서부터 증가하는 부분 수열을 구함.
# 정확히는 수열이 아니라 각각의(앞에서, 뒤에서) dp테이블에 해당 수를 기준으로 가장 긴 증가하는 부분 수열의 길이를 구함.
# 그리고 0부터 n까지 탐색을 다시 한 번 돌리며 dp와 reversed_dp의 값의 합이 가장 높은 것을 구함.
# 이때 애초에 각 dp테이블에 1이 초기화 되어 있으므로, 1을 빼서 중복을 피해주면 됌.
import sys
input = sys.stdin.readline

def logest_bitonic(seq, n):
    dp = [1] * n
    reversed_dp = [1] * n
    result = 0

    # 0에서 n까지 가장 긴 증가하는 부분 수열의 길이를 dp에 저장.
    for i in range(1, n):
        for j in range(i):
            if seq[j] < seq[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    # n에서 0까지 가장 긴 증가하는 부분 수열의 길이를 reversed_dp에 저장.
    for i in range(n - 2, -1, -1):
        for j in range(n - 1, i, -1):
            if seq[j] < seq[i]:
                reversed_dp[i] = max(reversed_dp[i], reversed_dp[j] + 1)
    
    # 각 dp테이블의 합을 구하고 중복 제거를 위해 1을 빼서 리턴.
    for i in range(n):
        result = max(result, dp[i] + reversed_dp[i])
    
    return result - 1
    

if __name__ == "__main__":
    N = int(input())
    seq = list(map(int, input().split()))
    print(logest_bitonic(seq, N))