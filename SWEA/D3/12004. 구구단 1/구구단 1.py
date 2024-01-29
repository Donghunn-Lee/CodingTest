# 구구단 1

def mulTable(N):
    for i in range(1, 10):
        for j in range(1, 10):
            if i*j == N:
                return "Yes"

    return "No"


T = int(input())

for t in range(1, T+1):

    N = int(input())

    ans = mulTable(N)

    print(f"#{t} {ans}")