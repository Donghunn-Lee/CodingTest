// 이름 궁합

const fs = require("fs");
const [A, B] = fs.readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt").toString().trim().split("\n");

const alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
const strokes = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1];
const alpha_strokes = {};

for (let i = 0; i < alpha.length; i++) {
    alpha_strokes[alpha[i]] = strokes[i]
}

let compatibility = [];
let result = '';

for (let i = 0; i < A.length; i++) {
    compatibility.push(alpha_strokes[A[i]]);
    compatibility.push(alpha_strokes[B[i]]);
}

while (2 < compatibility.length) {
    let tmp = [];

    for (let i = 1; i < compatibility.length; i++) {
        tmp.push((compatibility[i - 1] + compatibility[i]) % 10);
    }

    compatibility = tmp;
}

if (compatibility[0] === 0) {
    result = '0' + compatibility[1];
} else {
    result = compatibility.join("");
}

console.log(result);
