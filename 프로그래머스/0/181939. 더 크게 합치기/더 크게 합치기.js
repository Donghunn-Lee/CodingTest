function solution(a, b) {
    var answer = 0;
    a = a.toString();
    b = b.toString();
    
    return Math.max(+(a + b), +(b + a));
}