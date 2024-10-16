function solution(arr) {
    var answer = 0;
    let x = 0;
    
    while (true) {
        let tmp = [...arr];
        
        for (let i = 0; i < arr.length; i++) {
            if (50 <= arr[i] && arr[i] % 2 == 0) {
                arr[i] /= 2;
            } else if (arr[i] < 50 && arr[i] % 2 == 1) {
                arr[i] = arr[i] * 2 + 1;
            }
        }
        
        if (tmp.join("") === arr.join("")) {
            return x;
        }
        
        x++;
    }
    
    return answer;
}