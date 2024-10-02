function solution(q, r, code) {
    var answer = '';
    
    [...code].forEach((val, idx) => {
        if (idx % q === r) {
            answer += val;
        }
    })
    
    return answer;
}