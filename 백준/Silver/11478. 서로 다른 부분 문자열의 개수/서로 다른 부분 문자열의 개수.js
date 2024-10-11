// 서로 다른 부분 문자열의 개수

const fs = require("fs");
const str = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "input.txt")
  .toString()
  .trim();

function main() {
  const set = new Set();

  for (let i = 0; i < str.length; i++) {
    for (let j = 1; i + j <= str.length; j++) {
      set.add(str.slice(i, i + j));
    }
  }

  console.log(set.size);
}

main();
