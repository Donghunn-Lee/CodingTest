// 달팽이는 올라가고 싶다

const fs = require("fs");

function Input() {
    return fs.readFileSync(process.platform === "linux" ? "/dev/stdin" : "./baekjoon/JS/input.txt")
    .toString()
    .trim()
    .split(" ")
    .map(Number)
}


function sol() {
    let input = Input();
    let A = input[0], B = input[1], V = input[2];
    
    return Math.ceil((V - B) / (A - B));
}

console.log(sol());