# [S/W 문제해결 기본] 2일차 - Sum

T = 10
length=100
output=[]
for n in range(1, T+1) :
    t_num = int(input().strip())
    arr = []

    for i in range(length) :
        tmp = list(map(int,input().rstrip().split()))
        arr.append(tmp)
        
    max_sum = 0

    for i in range(length) :
        sum_row = 0
        sum_col = 0
        sum_cross_1 = 0
        sum_cross_2 = 0

        for j in range(length) :
            sum_row += arr[i][j]
            sum_col += arr[j][i]
            sum_cross_1 += arr[j][j]
            sum_cross_2 += arr[j][(length-1)-j]

        max_sum = max(sum_row, sum_col, sum_cross_1, sum_cross_2, max_sum)

    output.append("#{} {}".format(n, max_sum))

print("\n".join(output))
