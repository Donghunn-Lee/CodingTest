# 선분 교차 2

# 벡터 외적의 개념을 활용한 CCW(Counter Clock Wise)알고리즘을 사용해야 하는 문제.
# CCW는 A, B, C 세 개의 점을 이을 때 선분 AB를 기준으로 C가 시계방향인지, 반시계방향인지, 직선인지를 판단함.
# 너무 수학적인 문제이고, 전에 한 번 ccw문제를 풀었었는데 답이 없어서 보자마자 아 그거네 하고 검색.
import sys
input = sys.stdin.readline

def ccw(x1, y1, x2, y2, x3, y3):
    tmp = (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)

    if 0 < tmp:
        return 1
    
    elif tmp < 0:
        return -1
    
    else:
        return 0

def sol(x1, y1, x2, y2, x3, y3, x4, y4):
    ccw_ABC = ccw(x1, y1, x2, y2, x3, y3)
    ccw_ABD = ccw(x1, y1, x2, y2, x4, y4)
    ccw_CDA = ccw(x3, y3, x4, y4, x1, y1)
    ccw_CDB = ccw(x3, y3, x4, y4, x2, y2)
    flag = False
    ans = 0
    

    if ccw_ABC * ccw_ABD == 0 and ccw_CDA * ccw_CDB == 0:
        flag = True
        if min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2):
            ans = 1
    
    if ccw_ABC * ccw_ABD <= 0 and ccw_CDA * ccw_CDB <= 0:
        if not flag:
            ans = 1

    return ans

if __name__ == "__main__":
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())
    
    print(sol(x1, y1, x2, y2, x3, y3, x4, y4))