function solution(num_list) {
    var answer = 0;
    let oddSum = 0;
    let evenSum = 0;
    
    for (let i = 0; i < num_list.length; i++) {
        if (i % 2) {
            oddSum += num_list[i];
        } else {
            evenSum += num_list[i];
        }
    }
    
    return oddSum <= evenSum ? evenSum : oddSum;
    
}