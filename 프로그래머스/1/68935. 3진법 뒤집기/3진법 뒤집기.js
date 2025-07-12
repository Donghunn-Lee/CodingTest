function solution(n) {
    let result = 0;
    let tmp = Array();
    
    while (0 < n) {
        let q = 0;
        let r = 0;
        
        q = Math.floor(n / 3);
        r = n % 3;
        
        
        tmp.push(r);
        
        n = q;
    }
    
    for(let i = 1; i <= tmp.length; i++) {
        result += tmp[tmp.length - i] * (3 ** (i - 1));
    }
    
    return result;
    
}

