# # IOIOI

# # 처음부터 맞는 방향으로 접근해서 풀긴 했는데 풀고보니 조금 코드가 더럽긴 함.
# # if tmp 저 코드를 빼고 원래 find로 첫 I를 찾고 나서 하는 게 더 빠를까 하는 생각은 했는데,
# # 시간복잡도가 전체 루프에 if 검사가 더해지는 게 더 느린지 find가 느린지 정확히 몰랐음.
# # find가 더 빠르지 않을까 싶긴 했는데 우선 그냥 쓰지 않고 먼저 풀어 봄. 다소 느리지만 통과.

# import sys
# input = sys.stdin.readline

# # 문자열과 기준 길이를 입력.
# def IOI(s, n):
#     length = 2 * n + 1  # 기준 길이
#     elements = []   # IOI조합을 저장할 리스트
#     tmp = ''    # IOI 조합을 만드는 리스트
#     result = 0

#     # 문자열 전체를 돌며 IOI를 tmp에 만들고, IOI가 깨지면 만든 것을 element에 추가하고 tmp는 초기화.
#     for i in s:
#         if tmp:
#             if i == 'I' and tmp[-1] == 'O':
#                 tmp += i
#             elif i == 'O' and tmp[-1] == 'I':
#                 tmp += i
#             else:
#                 if len(tmp) % 2:
#                     elements.append(tmp)
#                 else:
#                     elements.append(tmp[:-1])
#                 if i == 'I':
#                     tmp = 'I'
#                 else:
#                     tmp = ''
#         else:
#             if i == 'I':
#                 tmp += i
    
#     # 입력 전체가 완전한 IOI여서 위 else 문이 실행되지 않는 경우를 대비한 코드.
#     if tmp:
#         if len(tmp) % 2:
#             elements.append(tmp)
#         else:
#             elements.append(tmp[:-1])
    
#     # 찾은 IOI 조합들의 길이를 계산해 그 안에서 기준길이가 몇 개 나올 수 있는지를 계산해 result에 저장.
#     for i in list(map(len, elements)):
#         if length < i:
#             result += (i - length) // 2 + 1
#         elif length == i:
#             result += 1
        
#     return result

# if __name__ == "__main__":
#     N = int(input())
#     M = int(input())
#     S = input().rstrip()

#     print(IOI(S, N))

# find를 이용해 시작점을 찾고, OI로 인덱스 2씩 진행하며 찾고, 확인한 문자열은 삭제하는 효율적인 답안이 있어서 저장.
import sys
# sys.stdin = open('data.txt', 'r')
input = sys.stdin.readline


def get_sub_cnt(string, start):
    cnt = 1
    while True:
        if string[start:start+2] == 'OI':
            cnt += 1
            start += 2
        else:
            return cnt
        
if __name__ == '__main__':
    n = int(input())
    length = int(input())
    string = input().strip()
    target = 'I' + 'OI' * n
    
    cnt = 0
    while True:
        target_idx = string.find(target)
        # find 함수는 조건에 만족하는 substring이 없다면 -1을 반환한다
        if target_idx == -1:
            break
        
        # string 내에 존재하는 가장 첫 substring을 확인 -> OI를 붙여가며 개수를 센다
        temp = get_sub_cnt(string, target_idx + len(target))
        cnt += temp
        # 확인이 끝나 필요없는 substring은 슬라이싱으로 제거한다.
        string = string[target_idx + len(target) + len('OI') * (temp - 1):]
    print(cnt)