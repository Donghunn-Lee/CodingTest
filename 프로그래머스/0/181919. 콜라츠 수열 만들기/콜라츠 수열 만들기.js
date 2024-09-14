function solution(n) {
    let arr = [];
    
    while (n != 1) {
        arr.push(n);
        
        if (n % 2) n = 3 * n + 1;
        else n /= 2;
    }
    
    arr.push(n);
    
    return arr;
}