# 펠린드롬?

import sys
input = sys.stdin.readline

def check_palindrome(is_pal):

    for i in range(N + 1):
        for start in range(1, N + 1 - i):
            end = start + i

            if start == end :
                is_pal[start][end] = 1
            
            elif seq[start] == seq[end]:
                if start + 1 == end:
                    is_pal[start][end] = 1
                
                elif is_pal[start + 1][end - 1]:
                    is_pal[start][end] = 1


if __name__ == "__main__":
    N = int(input())
    seq = [0] + list(map(int, input().split()))
    M = int(input())
    questions = []
    for _ in range(M):
        s, e = map(int, input().split())
        questions.append((s, e))

    is_pal = [[0] * (N + 1) for _ in range(N + 1)]
    check_palindrome(is_pal)
    
    ans = []

    for s, e in questions:
        ans.append(str(is_pal[s][e]))
    
    print("\n".join(ans))