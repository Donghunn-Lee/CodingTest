# RGB거리

# 대충 그냥 다 돌리면 되나 싶다가 dfs..? 하고 dp같아서 점화식을 어떻게 짜야 할지 고민함.
# 그렇게 작성한 코드로 예제가 다 맞아서 냈는데 시간초과.
# 재귀 방식 자체가 문제인지 아니면 계산식이 문제인지 모르겠으나 더 방법이 떠오르지 않아 검색.
# 한숨이 나올 정도로 단순한 코드. 그냥 다 돌리면 되는 게 맞았음.
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    costs = [list(map(int, input().split())) for _ in range(N)]

    # RGB중 한 값을 선택했을 때, 그 전 스탭에서 다른 두 색 중 최솟값을 고르고 현재 값을 더하는 방식.
    # R, G, B 각각 시작값을 정해야 하므로 셋 다 구해서 최솟값을 계산해야 함.
    for i in range(1, N):
        costs[i][0] = min(costs[i - 1][ 1], costs[i - 1][2]) + costs[i][0] 
        costs[i][1] = min(costs[i - 1][ 0], costs[i - 1][2]) + costs[i][1] 
        costs[i][2] = min(costs[i - 1][ 0], costs[i - 1][1]) + costs[i][2] 
    
    print(min(costs[N - 1][0], costs[N - 1][1], costs[N - 1][2]))