// 1546 평균

let input = require('fs').readFileSync('/dev/stdin').toString().split('\n');

const num = +input[0];
const score = input[1].split(" ").map(Number);

const max = Math.max(...score);
let sum = 0;

for(let i = 0; i < num; i++) {
    sum += score[i] / max * 100;
}

console.log(sum / num)