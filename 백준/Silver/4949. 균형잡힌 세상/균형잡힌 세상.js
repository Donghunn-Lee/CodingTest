// 균형잡힌 세상

const fs = require("fs");

function Input() {
    return fs.readFileSync(process.platform === "linux" ? "/dev/stdin" : "./baekjoon/JS/input.txt")
    .toString()
    .trim()
    .split("\n")
}

function sol() {
    input_data = Input();
    input_data.pop();
    let bracket_dict = {'(' : ')', ')' : '(', '[' : ']', ']' : '['}
    let ans = [];

    for (let i = 0; i < input_data.length; i++) {
        let stack = [];
        let flag = true;

        for (let c of input_data[i]) {
            if ("([".includes(c)) {
                stack.push(c);
            } else if (")]".includes(c)) {
                if (bracket_dict[c] === stack.at(-1)) {
                    stack.pop();
                } else {
                    flag = false;
                    ans.push("no");
                    break;
                }
            }
        }

        if (flag) {
            if ("([".includes(stack.at(-1))) {
                ans.push("no");
            } else {
                ans.push("yes");
            }

        }
    }

    return ans.join("\n");
}


console.log(sol());