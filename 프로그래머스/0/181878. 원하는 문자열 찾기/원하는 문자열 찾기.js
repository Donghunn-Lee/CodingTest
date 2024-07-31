function solution(myString, pat) {
    let arr = myString.toLowerCase().split(pat.toLowerCase());
    
    if (1 < arr.length){
        return 1;
    } else {
        return 0;
    }
}