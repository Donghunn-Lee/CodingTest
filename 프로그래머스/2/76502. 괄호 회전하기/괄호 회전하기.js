function solution(s) {
    let answer = 0;
    const n = s.length;

    const isValid = (str) => {
        const stack = [];
        const pair = { '}': '{', ']': '[', ')': '(' };

        for (const char of str) {
            if (!pair[char]) {
                stack.push(char);
            } else {
                if (stack.length === 0 || stack.pop() !== pair[char]) {
                    return false;
                }
            }
        }

        return stack.length === 0;
    };

    for (let i = 0; i < n; i++) {
        const rotatedStr = s.slice(i) + s.slice(0, i);

        if (isValid(rotatedStr)) {
            answer++;
        }
    }

    return answer;
}