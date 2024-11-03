let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let n = Number(input[0]);
let arr = input[1].split(" ").map(Number);

let m = Number(input[2])
let prefix = [0];
let result = []
for(let i = 3; i < m + 3; i++){
  let [a, b] = input[i].split(" ").map(Number);
  result.push([a, b]);
}
let summary = 0;

for(let i = 0; i < m; i++){
  summary += arr[i];
  prefix.push(summary);
}

for(let [left, right] of result){
  console.log(prefix[right] - prefix[left - 1]);
}