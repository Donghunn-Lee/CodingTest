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