function solution(arr, n) {
    var answer = [];
    
    if (arr.length % 2) {
        return arr.map((val, idx) => {
            if (idx % 2 == 0) {
                return val + n;
            }
            return val
        })
    } else {
        return arr.map((val, idx) => {
            if (idx % 2) {
                return val + n;
            }
            
            return val
        })
    }
    
    return answer;
}