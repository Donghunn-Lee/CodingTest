function solution(arr1, arr2) {
    let sumArr1 = arr1.reduce((sum, cur) => sum + cur);
    let sumArr2 = arr2.reduce((sum, cur) => sum + cur);
    
    var answer = arr1.length < arr2.length ? -1 : arr1.length > arr2.length ? 1 : sumArr1 < sumArr2 ? -1 : sumArr1 > sumArr2 ? 1 : 0;
    
    return answer;
}