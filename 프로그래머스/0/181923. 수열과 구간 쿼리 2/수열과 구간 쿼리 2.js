function solution(arr, queries) {
    var answer = [];
    
    for (let q of queries) {
        let tmp = Infinity;
        
        for (let i = q[0]; i <= q[1]; i++) {
            if (q[2] < arr[i]) {
                tmp = Math.min(tmp, arr[i]);
            }
        }
        
        if (tmp === Infinity) {
            tmp = -1;
        }
        
        answer.push(tmp);
    }
    
    return answer;
}