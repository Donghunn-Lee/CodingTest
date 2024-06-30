# 나이순 정렬

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    lst = [input().rstrip().split() for _ in range(N)]
    lst.sort(key = lambda x : int(x[0]))

    print("\n".join(map(" ".join, lst)))