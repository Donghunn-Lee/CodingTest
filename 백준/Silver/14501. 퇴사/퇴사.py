# 퇴사

# 코테 공부 거의 처음 시작할 때 접했던 문제. 결국 못 풀었던 게 생각나서 다시 풀어보려 했는데 실버 3인데도 불구하고
# 거의 3 시간은 쳐다본 듯. dp인 건 알겠는데 이걸 어떻게 더해가야 할지가 너무 막막했음.
# 그래도 결국 풀긴 풀었음. 상향식으로 max를 두 번이나 써서 풀었음. 분명 저게 다른 방법이 있을텐데 난 이게 최선.
# 찾아보니 대부분 하향식으로 풀고 있었음. 아직도 감을 덜 잡았다는 뜻.
import sys
input = sys.stdin.readline

def best_schedule(cl):
    dp = [0] * (N + 1)

    for i, (t, p) in enumerate(cl):
        if i + t <= N:
            dp[i + t] = max(dp[i + t], max(dp[:i + 1]) + p)

    return max(dp)
            
if __name__ == "__main__":
    N = int(input())
    consulution_list = [list(map(int, input().split())) for _ in range(N)]

    print(best_schedule(consulution_list))