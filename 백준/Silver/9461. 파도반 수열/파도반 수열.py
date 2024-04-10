# 파도반 수열

import sys
input = sys.stdin.readline

def fractal_triangle(n):
    seq = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

    for i in range(11, n + 1):
        seq.append(seq[i - 1] + seq[i- 5])

    print(seq[n])


if __name__ == "__main__":
    T = int(input())
    

    for _ in range(T):
        N = int(input())
        fractal_triangle(N)
    
    