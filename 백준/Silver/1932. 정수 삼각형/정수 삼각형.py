# 정수 삼각형

# 왜인지 당연하게 for문을 쓰다가 이게 아닌데? 하고 금방 정신 차림.
# DP 저장소 하나와 재귀함수로 풀 수 있었던 문제.
# 맨 아래층 값들을 리스트에 넣어두고, 더할 수 있는 위층 수에 아래의 두 수 중 더 큰 수를 더해 저장하는 방식.
# i열 j번 = i열 j번의 값 + (i + 1열 j번과 i + 1 열 j + 1번 중 더 큰 수)

# +++ 그냥 이렇게만 했다가 시간초과. 왜 났나 하니 dp[i][j]가 여러 번 초기화 되고 있었음.
# 왼쪽 위에서 한 번 호출해서 값이 할당되면 다음 이 자리를 방문하는 함수는 바로 리턴해야 하는데 그런 조건이 없었음.
# 그래서 dp값이 없는 경우에만 갱신하도록 if문 추가.
# import sys
# input = sys.stdin.readline

# def sum_down(dp, i, j):
#     if i == N - 1:
#         return dp[i][j]
    
#     if not dp[i][j]:
#         dp[i][j] = triangle[i][j] + max(sum_down(dp, i + 1, j), sum_down(dp, i + 1, j + 1))
    
#     return dp[i][j]
    

# if __name__ == "__main__":
#     N = int(input())
#     triangle = [list(map(int, input().split())) for _ in range(N)]
#     dp = [[0] * i for i in range(1, N)] + [triangle[N - 1]]
 
#     print(sum_down(dp, 0, 0))



# 나는 그런 문제를 많이 풀어서 그런지 DP하면 재귀, 그리고 그래프와 같이 쓰는 방식을 떠올리는데, 그냥 for도 써야 함.
# 아래는 풀고 나서 찾아본 보편적인 답안.
# for문을 쓰면 각 자리당 
# 1932  정수 삼각형 (파이썬 Python)

n = int(input())
dp = []

for i in range(n) :                            ## 입력값 이차원리스트 형태로 dp테이블에 저장하기
    dp.append(list(map(int,input().split())))

for i in range(1,n) :                           ## 행을 기준으로 for문 구성
    for j in range(0,i+1) :                     ## 열을 기준으로 for문 구성
        if j == 0 :
            dp[i][0] += dp[i-1][0]              # 0열끼리 더하기
        elif j == i :
            dp[i][j] += dp[i-1][j-1]            # 마지막 열끼리 더하기
        else :
            dp[i][j] += max(dp[i-1][j-1],dp[i-1][j])    # 두 화살표중 더 큰 경우 받아들이기

print(max(dp[n-1]))                 # n-1행에서의 최댓값 출력