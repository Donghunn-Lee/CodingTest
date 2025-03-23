function solution(n, w, num) {
    const h = Math.ceil(n / w)
    const garbage = Array.from(Array(h), () => Array(w).fill(0));
    let ans = 0;
    let cur = 1;
    let way = 1;
    let ci = 0, cj = 0;
    
    while (cur <= n) {
        garbage[ci][cj] = cur;
        cj += way
        
        if (cj === w) {
            way = -1;
            ci++;
            cj--;
        } else if (cj < 0) {
            way = 1;
            ci++;
            cj++;
        }
        
        cur++;
    }
    
    let ti

    if (num % w) {
        ti = Math.floor(num / w);
    } else {
        ti = num / w - 1;
    }

    let tj
    
    if (ti % 2) {
        tj = (w - (num % w || w)) % w;
    } else {
        tj = (num % w === 0) ? w - 1 : (num % w) - 1;
    }
    
    for (let i = ti; i < h; i++) {
        if (!garbage[i][tj]) return ans;
        
        ans++;
    }
    
    return ans;
}