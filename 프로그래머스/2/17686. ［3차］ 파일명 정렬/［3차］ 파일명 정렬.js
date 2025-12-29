function solution(files) {
    let answer = [];
    
    function normalizeFiles (files) {
        const newFiles = [];
        
        for (let file of files) {
            const parts = file.split(/([0-9]+)/);
            
            const head = parts[0];
            const number = parts[1];
            const tail = parts.slice(2).join('');
            
            newFiles.push({head, number, tail, src:file});
        }
        
        return newFiles;
    }
    
    const normFiles = normalizeFiles(files);
    
    normFiles.sort((a, b) => {
        const headA = a.head.toLowerCase();
        const headB = b.head.toLowerCase();
        
        // 문자열 비교 함수
        // headA가 headB보다 앞서면 -1, 뒤면 1, 같으면 0 반환
        const headCompare = headA.localeCompare(headB);
        if (headCompare !== 0) {
            return headCompare;
        }
        
        return parseInt(a.number) - parseInt(b.number);
    })
    
    answer = normFiles.map(file => file.src);
    
    return answer;
}