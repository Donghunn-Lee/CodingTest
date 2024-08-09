function solution(s, skip, index) {
    const N = s.length;
    var answer = '';
    
    skip = new Set([...skip].map((e) => e.charCodeAt()));
    
    for (const alpha of s) {
        let nxtAlpha = alpha.charCodeAt();
        nxtAlpha = 122 < nxtAlpha ? 96 + nxtAlpha - 122 : nxtAlpha;
        
        let i = 0;
        while (i < index) {
            nxtAlpha = nxtAlpha == 122 ? 97 : nxtAlpha + 1
            
            if (skip.has(nxtAlpha)) {
                continue;
            }
            
            i++;
        }

        answer += String.fromCharCode(nxtAlpha);
        
    }
        
    return answer;
}