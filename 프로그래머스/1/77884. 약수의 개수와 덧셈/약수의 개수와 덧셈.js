function findAllDivisor (arr, n) {
    for (let i = 2; i <= n; i++) {
        let cur = i;

        while(cur <= n) {
            arr[cur]++;
            cur += i;
        }
    }
}

function solution(left, right) {
    let ans = 0;
    const divisors = Array(right + 1).fill(1);
    findAllDivisor(divisors, right);
    
    for (let i = left; i <= right; i++) {
        if (divisors[i] % 2) {
            ans -= i;
        } else {
            ans += i;
        }
    }
    
    return ans;
}