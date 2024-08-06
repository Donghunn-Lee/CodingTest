// 소트인사이드

const fs = require("fs");

function Input() {
    return fs.readFileSync(process.platform === "linux" ? "/dev/stdin" : "./baekjoon/JS/input.txt")
    .toString()
    .trim()
    .split("")
    .map(Number);
}

function sol() {
    let input = Input();

    return input.sort((a, b) => b - a).join("");
}

console.log(sol());