// 직각삼각형

let fs = require("fs");

const Input = () => {
  return fs
    .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./baekjoon/JS/input.txt")
    .toString()
    .trim()
    .split("\n")
};

function sol() {
  let input_data = Input();
  var i = 0;

  while (true) {
    var each_side = input_data[i].split(' ').map(Number).sort((a, b) => {
      return a - b;
    });

    if (each_side.reduce((acum, cur) => acum + cur) === 0) {
      return;
    }

    let a = each_side[0] ** 2;
    let b = each_side[1] ** 2;
    let c = each_side[2] ** 2;
    let answer;

    if (a + b === c) {
      answer = "right";
    } else {
      answer = "wrong";
    }

    console.log(answer);

    i++;
  }
}

sol();