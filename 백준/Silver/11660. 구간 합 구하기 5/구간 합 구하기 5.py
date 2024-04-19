# 구간 합 구하기 5

# 당연히 안 될 걸 알고 그냥 sum으로 한 번 풀어봤다가 시간초과. 그저 시간 복잡도 계산을 해 보고 싶었음.
# 분류를 확인하니 그럴 것 같긴 했지만 dp이길래, 어떻게 활용할 수 있을까 고민하다가 해답을 떠올려냄.
# dp 테이블에 (0, 0)에서부터 어떤 좌표까지의 합을 계산하여 저장하면 약간의 계산으로 풀 수 있었음.

import sys
input = sys.stdin.readline

def cal_prefix_sum(dp, num_list):
    dp[0][0] = num_list[0][0]

    # 1행과 1열의 구간 합을 계산해 저장.
    for i in range(1, N):
        dp[i][0] = dp[i - 1][0] + num_list[i][0]
        dp[0][i] = dp[0][i - 1] + num_list[0][i]

    # 1,1부터 전체의 구간 합을 계산하여 해당 좌표에 저장.
    # (3, 3)위치의 구간 합을 구할 경우, (2, 3)의 구간합과 (3, 2)의 구간 합을 더하고,
    # 중복인 (2, 2)를 뺀 뒤 해당 위치의 값 num_list[3][3]을 더하면 (3, 3)의 구간 합을 구할 수 있음.
    for i in range(1, N):
        for j in range(1, N):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + num_list[i][j]


if __name__ == "__main__":
    N, M = map(int, input().split())
    num_list = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] * N for _ in range(N)]
    ans = []

    cal_prefix_sum(dp, num_list)

    for i in range(M):
        # 구간 합을 구할 좌표 입력. 1부터 시작되어 주어지므로 각 - 1.
        x1, y1, x2, y2 = map(int, input().split())
        x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
        
        # (x2, y2)의 구간 합에서 포함 안 되는 부분을 빼고,  두 번 차감된 (x1 - 1, y1 -1)를 한 번 더해 구간 합 계산.
        result = dp[x2][y2]
        
        # x1와 y1이 0이면 한 쪽만 빼 줘야 하므로 조건 추가.
        if x1 != 0 and y1 != 0:
            result -= dp[x2][y1 - 1] + dp[x1 - 1][y2]
            result += dp[x1 - 1][y1 - 1]
            ans.append(result)
            continue

        elif x1 == 0 and y1 == 0:
            ans.append(result)
            continue

        elif y1 == 0:
            result -= dp[x1 - 1][y2]
            ans.append(result)
            continue

        elif x1 == 0:
            result -= dp[x2][y1 - 1]
            ans.append(result)


                
        
            
    
    print("\n".join(map(str, ans)))