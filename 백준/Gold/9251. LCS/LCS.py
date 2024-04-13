# LCS

# dp는 정말 머리가 좋아야 풀 수 있구나 하는 생각이 들게 한 문제.
# 골드 5 따린데 요새 벽에 자주 막힘. 이 문제는 1시간동안 도저히 감도 잡히지 않아서 빠르게 검색함.
# 풀이를 보면 로직은 전혀 어렵지 않지만, 이 발상을 어떻게 하는 것인가에 대한 의문은 사라지지 않음.

# 아래와 같이 풀면 왼쪽 위부터 탐색한 사각형이 점점 커지며 그 범위 내에 존재하는 LCS의 길이를 구할 수 있음.
# 직접 그려보니 이해가 쉽게 되긴 하는데, 다시 말하지만 반나절을 들여도 나는 풀지 못할 것 같다는 게 결론.
# 진짜 결론은 많이 풀어서 유형을 외워버리자. 음.
import sys
input = sys.stdin.readline

def LCS(a, b):
    
    # 배열이 2개이므로 2차원 dp 리스트를 만들고 전체를 순회.
    dp = [[0] * len(b) for _ in range(len(a))]

    for i in range(1, len(a)):
        for j in range(1, len(b)):

            # 반복을 돌면서 문자가 같은 경우엔 리스트 평면상 왼쪽 위 값에서 + 1 해서 현재 위치에 저장.
            if a[i] == b[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1

            # 문자가 다른 경우엔 위와 왼쪽 값 중에 더 큰 값을 가져와서 저장.
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

    # 결국 리스트 끝에 LCS의 길이가 저장되므로 이를 반환.
    return dp[-1][-1]

if __name__ == "__main__":
    # 시작 값에 0을 두고 참조하기 위해 공백을 추가. (ex: 3*3 => 4*4)
    seq_A = ' ' + input().rstrip()
    seq_B = ' ' + input().rstrip()

    print(LCS(seq_A, seq_B))