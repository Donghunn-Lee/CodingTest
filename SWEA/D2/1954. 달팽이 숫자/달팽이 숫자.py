# 달팽이 숫자

T = int(input())
output = []

for t in range(1, T + 1) :
    N = int(input())
    snail = []
    for i in range(N) :
       snail.append([])
       for j in range(N) :
           snail[i].append(j+1+i*N)

    val, col, low, cur, s, new_start = 1, 0, 0, 0, 0, 0
    if N != 1 :
        while (val != (N*N+1)):
            if val in list(range(1+new_start, N*N+1, N-1-2*s)) :
                cur += 1
            if cur == 5 :
                cur = 1
                col, low = 0, 0
                s += 1
                new_start = val - 1

            if cur == 1 :
                snail[col+s][low+s] = val
                low += 1
            elif cur == 2 :
                snail[col+s][low+s] = val
                col += 1
            elif cur == 3 :
                snail[col+s][low+s] = val
                low -= 1
            elif cur == 4 :
                snail[col+s][low+s] = val
                col -= 1
                
            val += 1
    output.append(snail)
    print(f"#{t}")
    for i in range(N) :
        
        for j in range(N) :
            print(snail[i][j],end=' ')
        print()