function solution(targets) {
    let answer = targets.length ? 1 : 0;
    
    const sortedTargets = targets.slice().sort((a, b) => a[1] - b[1]);
    let curEnd = sortedTargets[0][1];
    
    for (let i = 1; i < sortedTargets.length; i++) {
        if (curEnd <= sortedTargets[i][0]) {
            answer++;
            curEnd = sortedTargets[i][1];
        }
    }
    
    return answer;
}