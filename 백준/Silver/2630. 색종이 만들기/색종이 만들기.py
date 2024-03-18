# 색종이 만들기

import sys
input = sys.stdin.readline

def cutting(cp, ci, cj, end):
    global count

    base_color = cp[ci][cj]

    if end == 1:
        count[base_color] += 1
        return
    

    for i in range(ci, ci + end):
        if (not base_color) in cp[i][cj : cj + end]:
            cutting(cp, ci, cj, end // 2)
            cutting(cp, ci + end // 2, cj, end // 2)
            cutting(cp, ci, cj + end // 2, end // 2)
            cutting(cp, ci + end // 2, cj + end // 2, end // 2)
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