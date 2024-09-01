const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const N = +input[0];
const divisor = input[1].split(" ").map(Number);

divisor.sort((a, b) => a - b);

console.log(divisor[0] * divisor.at(-1))