function solution(t, p) {
    var answer = 0;
    const N = +p;
    
    for (let i = 0; i <= t.length - p.length; i++) {
        if (+t.slice(i, i + p.length) <= N){
            answer++;
        }    
    }
    
    return answer;
}