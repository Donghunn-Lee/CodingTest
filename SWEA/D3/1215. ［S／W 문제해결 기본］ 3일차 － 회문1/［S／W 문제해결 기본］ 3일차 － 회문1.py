# 회문1

# 최근 펠린드롬 문제를 하나 풀어서 방식은 확인.
# bfs나 dfs로 한 번에 가로와 세로를 모두 탐색하려 했지만 너무 복잡해서 나눠서 각각 탐색.
# 찾는 길이가 4인 경우, 1번과 4번이 같으면 넘어가서 2번과 3을 비교하는 방식.

def find_palindrome():
    limit = 8 - L + 1
    count = 0

    # 가로 방향 탐색.
    for i in range(8):
        for j in range(limit):

            # 왼쪽과 오른쪽 포인터를 지정.
            # 펠린드롬이 아닌 경우 빠져나오기 위한 is_pal 변수.
            left, right = j, j + L - 1
            is_pal = True

            # 문자열을 모두 확인하거나 이미 펠린드롬이 아님을 확인할 때까지 반복.
            while left < right and is_pal:
                # 양 끝이 같으면 1칸 안쪽으로 포인터 이동.
                if graph[i][left] == graph[i][right]:
                    left += 1
                    right -= 1

                # 끝 값이 다른 경우 종료 조건 갱신.
                else:
                    is_pal = False

            # 반복 종료 후 is_pal 값에 따라 count + 1.
            if is_pal:
                count += 1

    # 같은 방식으로 세로 방향 탐색.
    for j in range(8):
        for i in range(limit):

            top, bottom = i, i + L - 1
            is_pal = True

            while top < bottom and is_pal:
                if graph[top][j] == graph[bottom][j]:
                    top += 1
                    bottom -= 1

                else:
                    is_pal = False

            if is_pal:
                count += 1
    
    return count


if __name__ == "__main__":
    ans = []

    for t in range(1, 11):
        L = int(input())
        graph = [list(input().rstrip()) for _ in range(8)]
    
        ans.append(f'#{t} {find_palindrome()}')

    print("\n".join(ans))