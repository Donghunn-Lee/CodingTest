# 별 찍기 - 11

# 전에 풀었던 Z라는 문제가 생각나서 재귀로 쉽게 풀리겠다고 생각함.
# 그런데 분명 이게 맞긴 한데 자꾸 왼쪽 아래 한 칸이 안 맞아서 1시간 돌파.
# 끝내 알아낸 원인은 별 개수가 너비 = 높이 * 2 - 1 이여서 함수에 입력을 N * 2 - 1로 했기 때문이었음.
# 아무튼 풀이는 전체 너비와 높이를 3개의 사각형으로 나누어서, 각각의 시작점과 사각형의 크기를 줄여가며 재귀호출.
# 가장 작은 삼각형이 들어가는 사각형은 너비 5에 높이 3짜리 이므로, 높이가 3일 때 *로 삼각형을 그림.
import sys
input = sys.stdin.readline
print = sys.stdout.write

def fractal_triangle(height, width, ci, cj):
    if height != 3:
        fractal_triangle(height // 2, width // 2, ci, cj + width // 4)
        fractal_triangle(height // 2, width // 2, ci + height // 2, cj)
        fractal_triangle(height // 2, width // 2, ci + height // 2, cj + width // 2)
    else:
        paper[ci][cj + 2] = '*'
        paper[ci + 1][cj + 1] = paper[ci + 1][cj + 3] = '*'
        paper[ci + 2][cj: cj + 5] = '*****' 


if __name__ == "__main__":
    N = int(input())
    paper = [[' ' for _ in range(N * 2 - 1)] for _ in range(N)]
    ans = ''

    fractal_triangle(N, N * 2, 0, 0)

    for i in paper:
        print(''.join(i)+'\n')