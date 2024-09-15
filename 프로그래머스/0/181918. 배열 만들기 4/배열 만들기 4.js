function solution(arr) {
    var stk = [];
    let i = 0;
    
    while (i < arr.length) {
        if (stk.length) {
            if (stk.at(-1) < arr[i]) {
                stk.push(arr[i]);
                i++;
            } else {
                stk.pop();
            }
        } else {
            stk.push(arr[i]);
            i++;
        }
    }

    return stk;
}