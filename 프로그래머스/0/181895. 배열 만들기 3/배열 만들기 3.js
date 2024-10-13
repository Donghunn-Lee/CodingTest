function solution(arr, intervals) {
    var answer = [];
    
    for (let se of intervals) {
        let [s, e] = se;
        answer.push(...arr.slice(s, e + 1));
    }
    
    return answer;
}