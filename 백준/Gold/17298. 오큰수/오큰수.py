# 오큰수

def NGE(seq):
    stack = [[0, seq[0]]]
    result = [0 for _ in range(len(seq))]

    for i, j  in enumerate(seq):
        if stack[-1][1] > j:
            stack.append([i, j])
        else:
            for k in range(len(stack) - 1, -1, -1):
                if stack[k][1] < j:
                    result[stack[k][0]] = str(j)
                    stack.pop()
                else:
                    break
            stack.append([i,j])
    for i, j in stack:
        result[i] = '-1'
    
    return ' '.join(result)


if __name__ == "__main__":
    N = int(input())
    sequnce_A = list(map(int, input().split()))

    print(NGE(sequnce_A))