# 잃어버린 괄호

# 어렵게 생각하다가 어찌어찌 풀고보니 생각보다 쉬웠던 문제.
# 만약 사칙연산이 모두 있었다면 두 배는 어려웠을 것 같음.
# eval 없이 식의 값을 더하는 함수를 짜 보려다가 포기. 다른 사람들의 방법을 참고해 볼 필요가 있음.
import sys
input = sys.stdin.readline

# 문자열 식을 입력받아 '-' 가 나오면 우선 괄호를 씌우고 더하다가 다시 '-'가 나오면 괄호를 닫고 다시 새로 엶.
# 만약 사칙연산이 모두 있었다면 두 배는 어려웠을 것 같음.
def add_parenthesis(eq):
    result = ''
    num = ''
    opened = False  # 괄호가 열려 있는지를 체크.

    for i in eq:
        if i == '-':
            if num:
                # 새 연산자를 만날 때마다 이전의 숫자를 결과 식에 넣어줌.
                # int 형 변환 후 다시 str 형 변환을 하는 이유는 eval에 식이 들어갔을 때
                # 00009 처럼 int 형인데 0이 먼저 오는 파이썬 코드는 에러가 발생하기 때문.
                result += str(int(num))
                num = ''
            if opened:
                result += ')-('
            else:
                result += '-('
                opened = True

        elif i == '+':
            if num:
                result += str(int(''.join(map(str, num))))
                num = ''
            result += i
        else:
            num += i

    # 반복이 끝났을 때 남아있는 num을 넣어주고, 괄호가 열려있는 경우 닫아줌.
    if num:
        result += str(int(''.join(map(str, num))))
    if opened:
        result += ')'
    
    return result

if __name__ == "__main__":
    equation = input().rstrip()
    
    print(eval(add_parenthesis(equation)))