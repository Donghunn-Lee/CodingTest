function solution(arr, idx) {
    var answer = -1;
    
    for (let i = 0; i < arr.length; i++) {
        if (idx <= i && arr[i] === 1) {
            answer = i;
            break;
        }
    }
    
    return answer;
}