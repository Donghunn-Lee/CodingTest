function solution(myString, pat) {
    var answer = 0;
    
    let newPat = [...pat];
    for (let i = 0; i < newPat.length; i++){
        if (newPat[i] === 'A'){
            newPat[i] = 'B';
        } else {
            newPat[i] = 'A';
        }
    };
    
    newPat = newPat.join('');
    
    for (let i = 0; i + newPat.length - 1 < myString.length; i++){
        if (myString.slice(i, i + newPat.length) === newPat){
            answer = 1;
            break;
        }
    }
    
    
    return answer;
}