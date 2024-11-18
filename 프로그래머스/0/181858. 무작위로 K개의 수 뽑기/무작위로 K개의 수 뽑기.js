function solution(arr, k) {
    const randomArr = [];
    
    for (let i = 0; i < arr.length; i++) {
        if (randomArr.length === k) {
            break;    
        }
        
        if (!randomArr.includes(arr[i])) {
            randomArr.push(arr[i]);
        }
    }

    if (randomArr.length < k) {
        return [...randomArr, ...Array(k - randomArr.length).fill(-1)];
    }
    
    return randomArr;
    
}