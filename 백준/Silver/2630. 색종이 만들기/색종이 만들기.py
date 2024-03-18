# 색종이 만들기

# 전에 Z라는 문제가 이것과 비슷한 느낌으로 정사각형을 쪼개는 형식이었음.
# 덕분에 풀이는 생각보다 쉽게 떠올릴 수 있었음.
import sys
input = sys.stdin.readline

# 원본 리스트와 각 행과 열의 시작점, 그리고 끝점(시작점에서부터 거리)을 입력.
# 한 정사각형 원소 전체가 하나로 통일되어야 1개의 색종이로 취급하므로 시작 원소를 base_color로 저장.
# 이후 전체를 확인하여 반대 색이 있을 경우 4등분 커팅하며 함수 재귀.
# 크기가 1이 되거나 반대 색이 발견되지 않은 경우, 맞는 전역 변수에 더하고 리턴.
def cutting(cp, ci, cj, end):
    # global count
    base_color = cp[ci][cj]
    half = end // 2

    if end == 1:
        count[base_color] += 1
        return

    for i in range(ci, ci + end):
        if (not base_color) in cp[i][cj : cj + end]:
            cutting(cp, ci, cj, half)   # 2 사분면                  2 1
            cutting(cp, ci + half, cj, half)    # 3 사분면          3 4
            cutting(cp, ci, cj + half, half)    # 1 사분면
            cutting(cp, ci + half, cj + half, half) # 4 사분면
            return
        
    count[base_color] += 1

    return

if __name__ == "__main__":
    N = int(input())
    color_paper = [list(map(int, input().split())) for _ in range(N)]
    count = [0, 0]

    cutting(color_paper, 0, 0, N)

    print(count[0])
    print(count[1])