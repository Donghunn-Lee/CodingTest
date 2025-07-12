const decoding = (arr) => {
    let secretMap = [];
    
    arr.forEach((val, idx) => {
        let tmp = [...val.toString(2)]
        let lack = arr.length - tmp.length;

        for (let i = 0; i < lack; i++) {
            tmp.unshift('0');
        }

        secretMap.push(tmp)
    })
    
    return secretMap;
}

function solution(n, arr1, arr2) {
    var answer = [];
    
    arr1 = decoding(arr1);
    arr2 = decoding(arr2);
    
    for (let i = 0; i < n; i++) {
        let tmp = [];
        for (let j = 0; j < n; j++) {
            if (arr1[i][j] == '0' && arr2[i][j] == '0') {
                tmp.push(' ');
            } else {
                tmp.push('#');
            }
        }
        
        answer.push(tmp.join(''));
    }
    
    return answer;
}