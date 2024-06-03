# ATM

import sys
input = sys.stdin.readline

def min_waiting(seq):
    seq.sort()
    wating_time, tmp = 0, 0

    for time in seq:
        tmp += time
        wating_time += tmp
    
    return wating_time


if __name__ == "__main__":
    N = int(input())
    seq = list(map(int, input().split()))
    print(min_waiting(seq))
