function solution(d, budget) {
    let answer = 0;
    
    d.sort((a, b) => a - b);
    
    for (const money of d) {
        if (0 <= budget - money) {
            budget -= money;
            answer++;
        }

    }
    
    return answer;
    
}