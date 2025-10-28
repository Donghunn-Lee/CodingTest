class MaxHeap {
    constructor () { this.h = []; }
    
    push(x) {
        const a = this.h; a.push(x);
        let i = a.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if(a[p] >= a[i]) break;
            [a[p], a[i]] = [a[i], a[p]];
            i = p;
        }
    }
    
    pop() {
        const a = this.h;
        if (a.length === 0) return undefined;
        const top = a[0];
        const last = a.pop();
        if (a.length > 0) {
            a[0] = last;
            let i = 0;
            while (true) {
                let l = 2 * i + 1, r = 2 * i + 2, m = i;
                if (l < a.length && a[l] > a[m]) m = l;
                if (r < a.length && a[r] > a[m]) m = r;
                if (m === i) break;
                [a[i], a[m]] = [a[m], a[i]];
                i = m;
            }
        }
        return top;
    }
    
    get size() {return this.h.length;}
}

function solution(n, k, enemy) {
    if (k >= enemy.length) return enemy.length;
    
    const heap = new MaxHeap();
    for (let i = 0; i < enemy.length; i++) {
        const e = enemy[i];
        heap.push(e);
        n -= e;
        
        if (n < 0) {
            if (k > 0) {
                const largest = heap.pop();
                n += largest;
                k--;
            }
            if (n < 0) return i;
        }
    }
    
    return enemy.length;
}