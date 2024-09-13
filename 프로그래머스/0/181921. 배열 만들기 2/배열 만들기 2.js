function solution(l, r) {
    let arr = [];
    
    for (let i = l; i <= r; i++) {
        let str = i.toString();
        let flag = true;
        
        for (let j = 0; j < str.length; j++) {
            if (str[j] == '0' || str[j] == '5') {
                continue;
            } else {
                flag = false;
                break;
            }
        }
        
        if (flag) {
            arr.push(+str);
        }
    }
    
    if (arr.length) {
        return arr;
    } else {
        arr.push(-1);
        return arr;
    }
}