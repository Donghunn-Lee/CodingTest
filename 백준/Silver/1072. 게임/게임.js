const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

let [x, y] = input[0].split(" ").map(Number);
let z = Math.floor( (100 * y / x));
let left = 1;
let right = 1000000000;
let ans = Infinity;
while (left <= right) {
  let mid = parseInt((left + right) / 2);
  let new_z = Math.floor( (100 * (y + mid) / (x + mid)));
  if (z !== new_z) {
    ans = Math.min(ans, mid);
    right = mid - 1;
  } else {
    left = mid + 1;
  }
}
if (ans === Infinity) console.log(-1);
else console.log(ans);