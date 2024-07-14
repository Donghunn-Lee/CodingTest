# 선분 그룹

# 수학 문제는 너무 어려움. 이런 걸 공부 없이 머리로 푸는 사람들은 얼마나 똑똑한 사람들일까?
# 우선 벡터 외적을 써야 하는 문제. 전에 두 번인가 접했던 Counter Clock Wise 알고리즘을 사용해야 함.
# 선분을 기준으로 점이 선분의 위쪽에 위치하는지 아래인지를 판별하는 공식을 사용해 선분의 교차 여부를 판별.
# 판별한 값으로 union-find를 실행. root 선분을 기록하며 선분 그룹을 생성.
# 생성된 선분 그룹의 수와 크기가 가장 큰 그룹에 속한 선분의 개수를 출력.
# union-find 자체는 단순한데, 선부의 교차판별이 핵심이었던 문제. 검색 후 이해하는데 시간이 좀 걸림. ccw는 70% 이해완.

import sys
input = sys.stdin.readline

def find(x):
    if x == root[x]:
        return x
    
    root[x] = find(root[x])

    return root[x]


def union(r1, r2):
    if r1 > r2:
        r1, r2 = r2, r1
    
    root[r2] = r1


# 벡터 외적으로 삼각형의 넓이를 구하는 공식을 이용, 선분 교차를 판별.
def check_cross(l1, l2):
    a = (l1[0], l1[1])
    b = (l1[2], l1[3])
    c = (l2[0], l2[1])
    d = (l2[2], l2[3])

    # 작은 쪽에서 큰 쪽으로 점의 순서를 맞춰줌.
    if a > b:
        a, b, = b, a
    if c > d:
        c, d = d, c

    # 선분 ab, ac, ad
    ab = (b[0] - a[0], b[1] - a[1])
    ac = (c[0] - a[0], c[1] - a[1])
    ad = (d[0] - a[0], d[1] - a[1])
    
    # 삼각형 넓이를 구하는 공식. |(x2 - x1)(y3 - y1) - (y2 - y1)(x3 - x1)|
    t1 = ab[0] * ac[1] - ab[1] * ac[0]  # 삼각형 abc의 넓이
    t2 = ab[0] * ad[1] - ab[1] * ad[0]  # 삼각형 abd의 넓이

    # 절댓값을 제거한 식의 값이 양수라면 점 3은 1과 2를 잇는 선분 위쪽에, 음수라면 아래쪽에 위치하게 됨.
    # 이를 바탕으로 선분 12를 기준으로 점 2와 3을 각각 계산.
    # 점 3과 4의 곱이 음수라면, 선분을 기준으로 점 3과 4가 반대쪽에 위치하는 것이므로 선분 12와 34는 교차함.
    # 양수라면 어느 위 또는 아래에 점 3, 4가 모두 위치한 것이므로 두 선분은 교차하지 않음.
    if t1 * t2 <= 0:

        # 예외 : 한 직선 위에 네 점이 모두 있는 경우.
        if t1 == 0 and t2 == 0:
            return a <= c <= b or a <= d <= b or c <= a <= d or c <= b <= d
        return True

    else:
        return False


if __name__ == "__main__":
    N = int(input())
    lines = []
    for _ in range(N):
        x1, y1, x2, y2 = map(int, input().split())
        lines.append((x1, y1, x2, y2))
    
    root = [i for i in range(N)]

    for i in range(N - 1):
        for j in range(i + 1, N):
            if check_cross(lines[i], lines[j]) and check_cross(lines[j], lines[i]):
                a, b = find(i), find(j)

                if a != b:
                    union(a, b)
    
    for i in range(N):
        find(i)

    print(len(set(root)))

    root.sort()
    cnt = 1
    max_cnt = 1

    for i in range(1, N):
        if root[i - 1] == root[i]:
            cnt += 1
        else:
            cnt = 1
        
        max_cnt = max(max_cnt, cnt)

    print(max_cnt)