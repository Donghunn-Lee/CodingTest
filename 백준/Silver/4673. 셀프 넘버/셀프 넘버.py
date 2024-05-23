# 셀프 넘버

import sys
input = sys.stdin.readline

def get_self_num(n):
    tmp = n

    while 0 < n:
        tmp += n % 10
        n //= 10
    
    return tmp

def sol(seq):
    

    for i in range(1, 10001):
        if seq[i]:
            continue
        i = get_self_num(i)

        while i <= 10000 and not seq[i]:
            seq[i] = 1
            i = get_self_num(i)


if __name__ == "__main__":
    seq = [0] * 10001
    ans = []

    sol(seq)

    for i in range(1, 10001):
        if not seq[i]:
            ans.append(str(i))

    print("\n".join(ans))