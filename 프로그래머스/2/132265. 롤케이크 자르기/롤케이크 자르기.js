function solution(topping) {
    let answer = 0;
    const n = topping.length;
    const stack_left = Array(n).fill(0);
    const stack_right = Array(n).fill(0);
    const kinds_left = new Set();
    const kinds_right = new Set();
    
    for (let i = 0; i < n; i++) {
        kinds_left.add(topping[i]);
        kinds_right.add(topping[n - 1 - i]);
        stack_left[i] = kinds_left.size;
        stack_right[n - 1 - i] = kinds_right.size;
    }
    
    for (let i = 0; i < n - 1; i++) {
        if (stack_left[i] === stack_right[i + 1]) {
            answer++;
        }
    }
    
    return answer;
}