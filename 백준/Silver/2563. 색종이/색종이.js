const fs = require("fs");

// example.txt 파일에서 데이터를 읽어옴
let input = fs.readFileSync(0).toString().trim().split("\n");

let arr = [];
for (var i = 0; i < 101; i++) {
  arr.push(new Array(101).fill(false));
}

let n = Number(input[0]);
for (var i = 0; i < n; i++) {
  let x = parseInt(input[i + 1].split(" ")[0].trim());
  let y = parseInt(input[i + 1].split(" ")[1].trim());

  for (var j = x; j < x + 10; j++) {
    for (var k = y; k < y + 10; k++) {
      arr[k][j] = true;
    }
  }
}

let result = 0;
for (var i = 1; i < 101; i++) {
  for (var j = 1; j < 101; j++) {
    if (arr[i][j]) result++;
  }
}

console.log(result);