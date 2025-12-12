const solution = (p) => {
    // 입력이 빈 문자열인 경우, 빈 문자열 반환
    if (p === '') return '';
    
    // 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리
    let count = 0;
    let u = '', v = '';
    
    for (let i = 0; i < p.length; i++) {
        p[i] === '(' ? count++ : count--;
        
        if (count === 0) {
            u = p.slice(0, i + 1);
            v = p.slice(i + 1);
            break;
        }
    }
    
    // u가 "올바른 괄호 문자열"인지 확인
    if (isCorrect(u)) {
        return u + solution(v);
    }
    
    // u가 "올바른 괄호 문자열"이 아닌 경우
    else {
        let answer = '(';
        answer += solution(v)
        answer += ')';
        
        // u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어 뒤에 붙임
        for (let i = 1; i < u.length - 1; i++) {
            answer += (u[i] === '(' ? ')' : '(')
        }
        
        return answer;
    }
}

const isCorrect = (str) => {
    let stackCount = 0;
    for (let char of str) {
        if (char === '(') {
            stackCount++;
        } else {
            if (stackCount === 0) return false;
            stackCount--;
        }
    }
    
    return true;
}