// 덩치

const fs = require("fs");

function Input() {
    return fs.readFileSync(process.platform === "linux" ? "/dev/stdin" : "./baekjoon/JS/input.txt")
    .toString()
    .trim()
    .split("\n")
}

function solution() {
    input_data = Input();
    let N = Number(input_data[0]);
    let students = input_data.slice(1).map((e) => e.split(" ").map(Number))
    let ranking = Array(N).fill(1);

    for (let i = 0; i < N; i++) {
        for (let j = i + 1; j < N; j++) {
            if (students[i][0] < students[j][0] && students[i][1] < students[j][1]) {
                ranking[i]++;
            } else if (students[i][0] > students[j][0] && students[i][1] > students[j][1]){
                ranking[j]++;
            }
        }
    }

    return ranking.join(" ");
}

console.log(solution());