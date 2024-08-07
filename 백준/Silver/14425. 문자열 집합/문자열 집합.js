// 문자열 집합

const fs = require("fs");

function Input() {
    return fs.readFileSync(process.platform === "linux" ? "/dev/stdin" : "./baekjoon/JS/input.txt")
    .toString()
    .trim()
    .split("\n")
}


function sol() {
    input_data = Input();
    const N = input_data[0].split(" ").map(Number)[0];
    const S = input_data.slice(1, 1 + N);
    const testString = input_data.slice(N + 1);
    const setString = new Set(S);
    let count = 0;

    for (let string of testString) {
        if (setString.has(string)) {
            count++;
        }
    }

    return count++;
}


console.log(sol());