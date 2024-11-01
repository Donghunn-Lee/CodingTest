function solution(myString, pat) {
    let ans = 0;
    
    for (let i = 0; i < myString.length; i++) {
        if (myString.slice(i, i + pat.length) === pat) {
            ans++;        
        }
    }
    
    return ans;
}