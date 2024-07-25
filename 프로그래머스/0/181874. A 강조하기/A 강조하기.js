function solution(myString) {
    var answer = [...myString].map((s) => {
        if (s === 'a') {
            return 'A';
        } else if (s !== 'A' && s === s.toUpperCase()) {
            return s.toLowerCase();
        } else {
            return s;
        }
    }).join("");
    
    return answer;
}