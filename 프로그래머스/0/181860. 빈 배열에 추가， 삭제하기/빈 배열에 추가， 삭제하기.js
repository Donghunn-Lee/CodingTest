function solution(arr, flag) {
    const result = [];
    
    for (let i = 0; i<flag.length; i++){
        if (flag[i]) {
             for (let j = 0; j < arr[i]*2; j++) {
                 result.push(arr[i]);
             }
        } else {
            for (let j = 0; j < arr[i]; j++){
                result.pop();
            }
        }
    }
    
    return result;
}