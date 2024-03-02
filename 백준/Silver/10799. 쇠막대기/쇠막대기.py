# 위가 내가 푼 거. 아래는 보고 살짝 벙찐 모범답안.
# 주어진 문자열에서 쇠막대기의 시작점들만 스택으로 쌓음.
# )가 나오면 현재 스택에서 하나를 제거.
# 레이저가 나오면 '시작점만 저장한 스택' = '잘리는 쇠 막대 수' 가 되어 한 번의 반복으로 끝남.
# 지금 다시 돌이켜보면 충분히 한 번의 반복으로 끝낼 수 있다고 생각했어야 하는데, 처음 든 생각을 전혀 의심하지 않고 이어나가서 레이저와 막대의 대조를 다시 반복해야하는 위 코드를 만들어냄.
def solution(parentheses):
    stack = []
    cutting_count = 0
    
    for ele in parentheses:
        if ele == '(':
            stack.append(ele)
            last = ele
        else:
            if last == '(':
                stack.pop()
                cutting_count += len(stack)
                last = ele
            else:
                stack.pop()
                cutting_count += 1
    return cutting_count
        
if __name__ == "__main__":
    parentheses = input()
    print(solution(parentheses))