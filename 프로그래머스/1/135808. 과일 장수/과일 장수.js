function solution(k, m, score) {
    var answer = 0;
    let box = [];
    
    score.sort((a, b) => a - b);

    while (0 < score.length || box.length == m) {
        if (box.length == m) {
            answer += (box.at(-1) * m);
            box = [];
        }
        
        box.push(score.pop());
    }
    
    return answer;
}