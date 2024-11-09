function solution(strArr) {
    let answer = Array(31).fill(0);
    
    for (const arr of strArr) {
        answer[arr.length] += 1;
    }
    
    return Math.max(...answer);
}