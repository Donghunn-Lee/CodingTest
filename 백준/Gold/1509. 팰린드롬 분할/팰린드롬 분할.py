# 팰린드롬 분할

# 어제에 이어 골드 1. 역시 벽이다.
# 그래도 이 문제는 어떻게 풀어 볼 각이 보이긴 했으나 보이기만 했을 뿐, 구현할 순 없었음.
# 모든 길이에 대해 자른 문자열 2등분해서 펠린드롬을 찾는 걸 생각했는데, 다시 보니 reverse 때문에 분명 시간초과였음.
# 검색해서 찾은 해답은 펠린드롬임을 구하는 2중 리스트에 dp를 같이 사용하는 방식.
# 모든 펠린드롬을 reverse를 사용하지 않고 구할 수 있어서 그 다음은 dp식만 잘 짜면 되는 거였음.
# 이런 문제를 다시 풀게 될 때 이런 방식도 있었음이 떠오르길 바람.

import sys
input = sys.stdin.readline

def palindrome_div(data):
    L = len(data)
    is_pal = [[0] * L for _ in range(L)]    # i(행 번호) 부터 j(열 번호)까지의 문자열이 펠린드롬임을 확인할 리스트.
    dp = [2500 for _ in range(L)] + [0]     # 각 길이까지의 펠린드롬 분할 수.

    # 길이가 1인 펠린드롬.
    for i in range(L):
        is_pal[i][i] = 1

    # 길이가 2인 펠린드롬. ex) AA, BB
    for i in range(L - 1):
        if data[i] == data[i + 1]:
            is_pal[i][i + 1] = 1
    
    # 앞서 구한 길이 1, 2 펠린드롬을 기반으로 3부터 L까지의 펠린드롬 구하기.
    for i in range(3, L + 1):
        for start in range(L - i + 1):  # 길이에 따른 마지막 인덱스 계산 유의.
            end = start + i - 1
            
            # start와 end의 문자가 같고, 그 안이 펠린드롬인 경우. ex) ADA => 처음과 끝 문자가 같고, D는 길이 1.
            # 구한 길이 1 펠린드롬을 기반으로 길이 3을 구하고, 길이 2를 기반으로 길이 4를 구해가는 방식.
            if data[start] == data[end] and is_pal[start + 1][end - 1]:
                is_pal[start][end] = 1

    # 구한 모든 펠린드롬을 기반으로 dp를 계산.
    # dp[end]는 입력 문자열의 end번째 문자까지의 최소 펠린드롬 분할 수.
    # 따라서 최종 구하려는 값은 dp[L - 1]이 되며, 0부터 상향식으로 계산.
    for end in range(L):
        for start in range(end + 1):

            # start 부터 end까지가 펠린드롬인 경우,
            # 원래의 dp[end]값에 직전 길이 dp[start - 1]의 값에 1 (start부터 end의 펠린드롬 )을 더해 작은 값을 갱신.
            if is_pal[start][end]:
                dp[end] = min(dp[end], dp[start - 1] + 1)
            
            # 펠린드롬이 아니라면 그냥 직전 길이의 문자열 문자 하나가 추가된 것이므로 dp[end - 1] + 1.
            else:
                dp[end] = min(dp[end], dp[end - 1] + 1)

    return dp[L - 1]

if __name__ == "__main__":
    data = list(input().rstrip())
    print(palindrome_div(data))
