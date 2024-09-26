// 알고리즘 수업 - 피보나치 수 2

const fs = require("fs");
const N = +fs
  .readFileSync(process.platform == "linux" ? "/dev/stdin" : "input.txt")
  .toString()
  .trim();

const MOD = 1_000_000_007;

let temp1 = 1;
let temp2 = 1;
let temp3 = 0;

for (let i = 3; i <= N; i++) {
  temp3 = (temp1 + temp2) % MOD;
  temp1 = temp2;
  temp2 = temp3;
}
const fibo1 = temp3;
const fibo2 = N - 2;
console.log(`${fibo1} ${fibo2}`);
