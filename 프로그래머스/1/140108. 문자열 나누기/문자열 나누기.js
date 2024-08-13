function solution(s) {
    let curString = s[0];
    let subStrings = [];
    let correct = 1;
    let wrong = 0;
    
    let i = 1;
    while (i < s.length) {
        curString += s[i];
        
        if (s[i] === curString[0]) {
            correct++;
        } else {
            wrong++;
        }
        
        if (correct === wrong){
            subStrings.push(curString);
            curString = '';
        }
        
        i++;
    }
    
    if (curString) {
        subStrings.push(curString);
    }
    
    
    return subStrings.length;
}