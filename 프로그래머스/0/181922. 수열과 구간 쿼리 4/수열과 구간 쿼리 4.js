function solution(arr, queries) {
    for (let q of queries) {
        for (let i = q[0]; i <= q[1]; i++) {
            if (i % q[2] === 0) {
                arr[i]++;
            }
        }
    }
    
    return arr;
}