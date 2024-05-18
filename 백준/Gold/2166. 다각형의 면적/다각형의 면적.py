# 다각형의 면적

# 딱 봐도 수학 공식이 필요해 보여서 바로 검색.
# 벡터 외적을 사용해 다각형의 넓이를 구하는 건 알겠는데, 그 공식을 제대로 이해하진 못함.
# 굳이 외울 필요 없는 수학적인 부분이라 생각하고 그냥 대충 알고 넘어감.
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    x_list, y_list = [], []

    for _ in range(N):
        x, y = map(int, input().split())
        x_list.append(x)
        y_list.append(y)
    
    x_list.append(x_list[0])
    y_list.append(y_list[0])

    left, right = 0, 0

    for i in range(N):
        left += x_list[i] * y_list[i + 1]
        right += x_list[i + 1] * y_list[i]
    
    ans = round(abs(left - right) / 2, 1)

    print(ans)