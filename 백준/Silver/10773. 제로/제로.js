// 제로

const fs = require("fs");
const file = process.platform === "linux" ? "dev/stdin" : "./baekjoon/JS/input.txt";
const input = fs.readFileSync(file).toString().trim().split("\n").map(Number);

function sol() {
    input.shift()
    let stack = [];

    for (const i of input) {
        if (i !== 0) {
            stack.push(i);
        } else {
            stack.pop();
        }
    }

    if (stack.length === 0) {
        return 0;
    }

    return stack.reduce((acc, cur) => acc + cur);
}

console.log(sol());