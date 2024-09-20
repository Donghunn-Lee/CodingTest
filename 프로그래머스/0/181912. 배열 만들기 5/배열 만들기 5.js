function solution(intStrs, k, s, l) {
    let answer = [];
    
    for (let i = 0; i < intStrs.length; i++) {
        let tmp = +intStrs[i].slice(s, s + l);
        
        if (k < tmp) {
            answer.push(tmp);
        }
    }
    
    return answer;
}