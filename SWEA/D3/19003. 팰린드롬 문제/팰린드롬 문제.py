# 팰린드롬 문제

def pellendrom (arr) :
    for i in range(len(arr)) :
        tmp = []
        global single, couple 
        for j in range(1, len(arr[0]) + 1) :
            tmp.append(arr[i][-j])
        for k in range(len(arr)) :
            if "".join(tmp) == arr[k] and k!= i :
                couple += len(arr[k]) * 2
                if k < i :
                    del arr[i]
                    del arr[k]
                else :
                    del arr[k]
                    del arr[i]
                return pellendrom(arr)
        if arr[i] == ''.join(tmp) and single == 0 :
            single = len(arr[i])
            del arr[i]
            return pellendrom(arr)
    return single + couple

T = int(input())

for t in range(1, T + 1) :
    n, m = map(int, input().split())
    arr = []
    pel_len, single, couple = 0, 0, 0
    for i in range(n):
        arr.append(input())
    pel_len = pellendrom(arr)
    print(f"#{t} {pel_len}")