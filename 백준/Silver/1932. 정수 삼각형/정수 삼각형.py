# 정수 삼각형

# 왜인지 당연하게 for문을 쓰다가 이게 아닌데? 하고 금방 정신 차림.
# DP 저장소 하나와 재귀함수로 풀 수 있었던 문제.
# 맨 아래층 값들을 리스트에 넣어두고, 더할 수 있는 위층 수에 아래의 두 수 중 더 큰 수를 더해 저장하는 방식.
# i열 j번 = i열 j번의 값 + (i + 1열 j번과 i + 1 열 j + 1번 중 더 큰 수)

# +++ 그냥 이렇게만 했다가 시간초과. 왜 났나 하니 dp[i][j]가 두 번씩 초기화 되고 있었음.
# 왼쪽 위에서 한 번 호출, 오른쪽 위에서 한 번 호출 이렇게 같은 자리에 대한 함수가 두 번 실행.
# 그래서 dp값이 없는 경우에만 갱신하도록 if문 추가.
import sys
input = sys.stdin.readline

def sum_down(dp, i, j):
    if i == N - 1:
        return dp[i][j]
    
    if not dp[i][j]:
        dp[i][j] = triangle[i][j] + max(sum_down(dp, i + 1, j), sum_down(dp, i + 1, j + 1))
    
    return dp[i][j]
    

if __name__ == "__main__":
    N = int(input())
    triangle = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] * i for i in range(1, N)] + [triangle[N - 1]]
 
    print(sum_down(dp, 0, 0))