const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = 0;

rl.on("line", (line) => {
  input = line;
}).on("close", () => {
  const N = +input;
  let memoA = 1n;
  let memoB = 1n;
  for (let i = 2; i <= N; i++) {
    const prevA = memoA;
    const prevB = memoB;
    memoA = BigInt(prevA + prevB * 2n);
    memoB = BigInt(prevA + prevB);
  }
  console.log(((memoA + memoB * 2n) % 9901n).toString());
});