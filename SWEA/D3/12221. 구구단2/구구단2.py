# 구구단 2

T = int(input())

for t in range(1, T+1):
    A, B = map(int, input().split())

    if 9 < A or 9 < B:
        print(f"#{t} -1")
    else:
        print(f"#{t} {A*B}")
