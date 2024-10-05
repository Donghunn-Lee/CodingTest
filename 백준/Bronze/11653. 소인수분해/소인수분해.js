let input = require('fs').readFileSync(0,{encoding:"utf-8"}).split("\n").map(Number);

let N = input.shift();
const answer = [];

for (let i = 2; i <= N; i++) {
  while (N % i === 0) {
    N /= i;
    answer.push(i);
  }
  if (N === 1) break;
}

answer.forEach((number) => console.log(number));