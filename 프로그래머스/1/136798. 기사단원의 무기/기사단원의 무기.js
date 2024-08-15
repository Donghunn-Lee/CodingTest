function solution(number, limit, power) {
    var answer = 0;
    
    const divisors = Array(number + 1).fill(1);    
    
    for (let i = 2; i <= number; i++) {
        let n = i;
        
        while(n <= number) {    
            divisors[n] += 1;
            n += i;
        }
    }
    
    
    for (let i = 1; i <= number; i++) {
        let weaponPower = limit < divisors[i] ? power : divisors[i];
        answer += weaponPower;
    }
    
    return answer;
}