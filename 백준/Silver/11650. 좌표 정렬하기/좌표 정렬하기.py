# 좌표정렬하기

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    coordinate = [list(map(int, input().split())) for _ in range(N)]
    print("\n".join(map(lambda x : " ".join(map(str, x)), sorted(coordinate, key = lambda x : (x[0], x[1])))))