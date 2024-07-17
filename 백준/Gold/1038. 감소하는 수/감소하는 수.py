# 감소하는 수

import sys
input = sys.stdin.readline

def check_decreasing_num(n):
    one_digit = '0123456789'
    length = 1
    
    for i in one_digit:
        decreasing_num.append(i)

    while length < 10:
        for i in decreasing_num:
            if len(i) == length:
                for j in range(10):
                    if int(i[-1]) > j:
                        decreasing_num.append(i + str(j))
        
        length += 1
    
    if 1022 < n:
        return(-1)
    else:
        return(decreasing_num[n])


if __name__ == "__main__":
    N = int(input())
    decreasing_num = []
    
    print(check_decreasing_num(N))