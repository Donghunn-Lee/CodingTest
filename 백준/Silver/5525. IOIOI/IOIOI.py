# IOIOI

import sys
input = sys.stdin.readline

def IOI(s, n):
    length = 2 * n + 1
    elements = []
    tmp = ''
    result = 0

    for i in s:
        if tmp:
            if i == 'I' and tmp[-1] == 'O':
                tmp += i
            elif i == 'O' and tmp[-1] == 'I':
                tmp += i
            else:
                if len(tmp) % 2:
                    elements.append(tmp)
                else:
                    elements.append(tmp[:-1])
                if i == 'I':
                    tmp = 'I'
                else:
                    tmp = ''
        else:
            if i == 'I':
                tmp += i
    
    if tmp:
        if len(tmp) % 2:
            elements.append(tmp)
        else:
            elements.append(tmp[:-1])
    
    for i in list(map(len, elements)):
        if length < i:
            result += (i - length) // 2 + 1
        elif length == i:
            result += 1
        
    return result

if __name__ == "__main__":
    N = int(input())
    M = int(input())
    S = input().rstrip()

    print(IOI(S, N))