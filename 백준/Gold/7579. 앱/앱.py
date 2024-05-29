# 앱

# 호기롭게 정렬만으로 풀어봤는데 안됌.
# 방법은 냅색 알고리즘이었음. 기본중에 기본이지만 아직도 잘 이해가 안되는 어려운 dp 알고리즘.
# 개념은 앱의 개수를 N으로, 비용을 열로 하는 dp테이블 생성.
# 행과 열의 모든 칸을 반복하면서 값을 갱신.
# i번째 앱을 비활성화 할 때, i - 1개를 비활성화 시켰을 때의 메모리와, i - 1개일 때 비활성화한 앱 대신 지금 확인중인 앱을 비활성화시켰을 때의 메모리를 비교해 최댓값을 저장함.
# 위 내용이 전부이긴 한데, 그게 직관적으로 잘 이해가 안 됌. 그래도 지금 조금 더 이해도가 상승한 듯함.

import sys
input = sys.stdin.readline

def knapsack():
    dp = [[0] * (length) for _ in range(N + 1)]

    for i in range(1, N + 1): # i 개의 앱 비활성화
        for j in range(length): # 사용 가능한 비활성화에 필요한 비용
            # 현재 확인중인 비용 j보다 낮아서 비활성화 시킬 수 있는 경우
            if costs[i - 1] <= j: 
                dp[i][j] = max(memories[i - 1] + dp[i - 1][j - costs[i - 1]], dp[i - 1][j])

            else: # 비활성화 불가
                dp[i][j] = dp[i - 1][j]

    for i, c in enumerate(dp[-1]): # 
        if c >= M: # 처음으로 필요한 메모리보다 확보된 양이 많아진다면 출력
            return i

if __name__ == "__main__":
    N, M = map(int, input().split())
    memories = list(map(int, input().split()))
    costs = list(map(int, input().split()))
    length = sum(costs) + 1

    print(knapsack())