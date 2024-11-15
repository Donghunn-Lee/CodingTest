function solution(arr) {
    let i = 1;
    
    while (i < arr.length) {
        i *= 2;
    }
    
    let zeros = Array(i - arr.length).fill(0);
    
    return [...arr, ...zeros];
    
    
}