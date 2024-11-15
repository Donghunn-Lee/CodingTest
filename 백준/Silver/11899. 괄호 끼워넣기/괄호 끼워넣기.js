const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const arr = require("fs").readFileSync(filePath).toString().trim().split("");

const leftBracket = [];
const rightBracket = [];

for (let bracket of arr) {
  if (bracket === "(") {
    leftBracket.push(bracket);
  } else if (bracket === ")") {
    if (leftBracket.length > 0) {
      leftBracket.pop();
    } else {
      rightBracket.push(bracket);
    }
  }
}

console.log(leftBracket.length + rightBracket.length);
