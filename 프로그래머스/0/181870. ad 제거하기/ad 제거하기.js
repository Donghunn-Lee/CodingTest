function solution(strArr) {
    let answer = [];
    
    for (let arr of strArr) {
        if (!arr.includes('ad')) {
            answer.push(arr);
        }
    }
    
    return answer;
}