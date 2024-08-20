function solution(a, b, n) {
    var answer = 0;
    
    while(a <= n) {
        let  received = Math.floor(n / a) * b;
        answer += received;
        n = received + n % a;
    }
    
    return answer;
}