function solution(progresses, speeds) {
    let answer = [];
    const n = progresses.length;
    let cur = 0;
    
    while (cur < n) {
        let complete = 0;
        
        for (let i = 0; i < n; i++) {
            if (progresses[i] < 100) progresses[i] += speeds[i];
        }
        
        for (let i = cur; i < n; i++) {
            if (progresses[i] >= 100) {
                complete++;
                cur++;
            } else break;
        }
        
        if (complete) answer.push(complete);
    }
    
    return answer;
}