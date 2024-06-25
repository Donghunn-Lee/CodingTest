# 수 찾기
import sys
input = sys.stdin.readline

def find_num():
    ans = []

    for i in target:
        if i in A:
            ans.append('1')
        else:
            ans.append('0')
    
    return "\n".join(ans)


if __name__ == "__main__":
    N = int(input())
    A = set(map(int, input().split()))
    M = int(input())
    target = list(map(int, input().split()))

    print(find_num())