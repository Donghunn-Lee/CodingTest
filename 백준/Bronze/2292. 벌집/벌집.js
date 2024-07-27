// 벌집

const fs = require("fs");

function Input() {
    return Number(fs.readFileSync(process.platform === "linux" ? "/dev/stdin" : "./baekjoon/JS/input.txt"))
}

function sol() {
    let N = Input();
    let layer = 2;
    let i = 1;
    
    while (N >= layer) {
        layer += i * 6;
        i++;
    }

    console.log(i);
}

sol();