function solution(arr, queries) {
    for (let q of queries) {
        let tmp = arr[q[0]];
        arr[q[0]] = arr[q[1]];
        arr[q[1]] = tmp;
    }
    
    
    return arr;
}