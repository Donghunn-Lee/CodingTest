# 펠린드롬?

# 처음엔 무식하게 주어진 질문의 양 끝점에서부터 펠린드롬인지를 매번 탐색. 당연히 시간초과.
# 이후 2차원 dp테이블을 만들고 i부터 j까지 문자열의 펠린드롬 여부를 저장하는 방법을 떠올림.
# 하지만 그것도 모든 길이에 대해 처음 썼던 방식으로 펠린드롬 여부를 체크하니 시간초과가 발생함.
# dp의 꽃은 memoization. 앞서 구한 값을 활용해야했음.
# 그 밖에 조금 헷갈린 부분이 있다면, 처음엔 길이가 홀수인 문자열에서만 펠린드롬 여부를 확인할 수 있는 줄 알았음.

# 길이 1짜리부터 N짜리 펠린드롬을 순서대로 모두 구함.
# 구하는 과정에서, 양 끝점의 문자가 같다면 그 사이의 문자열이 펠린드롬인지 확인하여 현재 양 끝점의 펠린드롬 여부를 체크.
# 작은 길이부터 긴 길이 순으로 갱신하므로, 길이 3의 문자열을 탐색할 땐 이미 구한 길이 1의 펠린드롬 값을 활용 가능.
import sys
input = sys.stdin.readline

def check_palindrome(is_pal):
    for length in range(N + 1):
        for start in range(1, N + 1 - length):
            end = start + length

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