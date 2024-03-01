# 단어 뒤집기 2

S = input()

# 문자열 S내의 단어와 태그를 tmp에 넣어 구분함으로써 조건에 맞는 단어들을 뒤집어 반환하는 함수.
def reverse_word2(s):
    ans = []
    tag = False
    tmp = []

    for i in s:
        # < 를 먼저 검사할 경우, tag를 True로 바꾼 시점에서 무한루프이므로 >를 먼저 검사함.

        # > 를 발견한 경우, tag를 False로 다시 돌려주고 현tmp를 ans에 추가.
        if i == '>':
            tag = False
            ans.append('<'+''.join(tmp[1:])+'>')    # <>의 경우 한 쌍만 주어지므로 append 없이 직접 사용.
            tmp = []

        # < 를 발견한 경우, tmp에 문자가 들었다면 우선 뒤집어 ans에 추가.
        # tmp는 비워서 이후 <> 안의 문자를 담음.
        # tag를 True로 바꾸어 >를 만날 때 까지 해당 문을 반복하도록 함.
        elif i == '<' or tag:       
            if tmp and not tag: 
                tmp.reverse()
                ans.append(''.join(tmp))
                tmp = []
            tmp.append(i)
            tag = True      
        
        # 공백인 경우 tmp을 확인하여 문자가 있다면 뒤집어 ans에 넣은 후 다음 단어를 위해 초기화.
        elif i == ' ':
            if tmp:
                tmp.reverse()
                tmp.append(i)
                ans.append(''.join(tmp))
                tmp = []
        else:
            tmp.append(i)

    # 마지막이 항상 태그로 끝나면 문제 없지만, 단어로 끝날 때를 위해 반복 종료 후 tmp 확인 후 반환.
    if tmp:
        tmp.reverse()
        ans.append(''.join(tmp))

    return ''.join(ans)

print(reverse_word2(S))