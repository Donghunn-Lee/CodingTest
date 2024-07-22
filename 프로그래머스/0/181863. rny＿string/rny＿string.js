function solution(rny_string) {
    var answer = '';
    
    let i = 0;
    while (i < rny_string.length) {
        if (rny_string[i] === 'm') {
            answer += 'rn';
        } else {
            answer += rny_string[i]
        }
        
        i += 1
    }
    
    return answer;
}