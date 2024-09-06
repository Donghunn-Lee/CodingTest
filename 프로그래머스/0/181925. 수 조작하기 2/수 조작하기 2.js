function solution(numLog) {
    var answer = '';
    let n = numLog[0];
    
    for (let i = 1; i < numLog.length; i++) {
        if (numLog[i] === n + 1) {
            n++;
            answer += 'w';
        } else if (numLog[i] == n - 1) {
            n--;
            answer += 's';
        } else if (numLog[i] == n + 10) {
            n += 10;
            answer += 'd';
        } else if (numLog[i] == n - 10) {
            n -= 10;
            answer += 'a';
        }
    }
    
    return answer;
}