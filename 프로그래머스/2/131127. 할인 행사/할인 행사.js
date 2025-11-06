function solution(want, number, discount) {
    let answer = 0;
    
    const basket = {};
    for (let i = 0; i < want.length; i++) {
        basket[want[i]] = number[i];
    }
    let bCount = number.length;
    
    for (let i = 0; i < discount.length; i++) {
        if (basket[discount[i - 10]] !== undefined) {
            basket[discount[i - 10]] += 1;
            if(basket[discount[i - 10]] === 1) bCount++;
        }
        
        if (basket[discount[i]] === undefined) continue;
        
        if (basket[discount[i]] > 1) {
            basket[discount[i]] -= 1;
        } else {
            basket[discount[i]] -= 1;
            if (basket[discount[i]] === 0) bCount--;
        }
        
        if (bCount === 0) {
            answer++;
        }
    }
    return answer;
}