const fs = require("fs");
const file = process.platform === "linux" ? "dev/stdin" : "./text.txt";
const input = fs.readFileSync(file).toString().trim().split(" ");

const [n, k] = input.map(Number);

let parent = 1;
let child = 1;

for (i = 0; i < k; i++) {
  parent *= n - i;
  child *= k - i;
}

console.log(parent / child);