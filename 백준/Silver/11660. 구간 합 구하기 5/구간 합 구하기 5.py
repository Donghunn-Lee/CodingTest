# 구간 합 구하기 5

# 당연히 안 될 걸 알고 그냥 sum으로 한 번 풀어봤다가 시간초과. 그저 시간 복잡도 계산을 해 보고 싶었음.
# 분류를 확인하니 그럴 것 같긴 했지만 dp이길래, 어떻게 활용할 수 있을까 고민하다가 해답을 떠올려냄.
# num_list 테이블에 (0, 0)에서부터 어떤 좌표까지의 합을 계산하여 저장하면 약간의 계산으로 풀 수 있었음.
import sys
input = sys.stdin.readline

def cal_prefix_sum(num_list):
    # 1,1부터 각 좌표까지의 합을 계산하여 해당 좌표에 저장.
    # (3, 3)위치의 합을 구할 경우, (2, 3)까지의 합과 (3, 2)까지의 합을 더하고,
    # 중복인 (2, 2)를 뺀 뒤 해당 위치의 값 num_list[3][3]을 더하면 (0, 0)부터 (3, 3)의 합을 구할 수 있음.
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            num_list[i][j] += num_list[i - 1][j] + num_list[i][j - 1] - num_list[i - 1][j - 1]


if __name__ == "__main__":
    N, M = map(int, input().split())
    num_list = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
    ans = []

    cal_prefix_sum(num_list)

    for i in range(M):
        x1, y1, x2, y2 = map(int, input().split())

        # 합이 저장된 리스트로 구간합을 구하려면, 해당 좌표의 합에서 구간에 없는 부분들을 빼고 두 번 빼진 부분을 더함.
        ans.append(num_list[x2][y2] - num_list[x1 - 1][y2] - num_list[x2][y1 - 1] + num_list[x1 - 1][y1 - 1])


    print("\n".join(map(str, ans)))