function solution(num_list) {
    let [odd, even] = ['', ''];
    
    for (let i of num_list) {
        if (i % 2) {
            odd += i.toString();
        } else {
            even += i.toString();
        }
    }
    
    return +odd + +even;
}