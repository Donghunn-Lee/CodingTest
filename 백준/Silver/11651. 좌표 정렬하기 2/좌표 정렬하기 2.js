const fs = require("fs");

function Input() {
    return fs.readFileSync(process.platform === "linux" ? "/dev/stdin" : "./baekjoon/JS/input.txt")
    .toString()
    .trim()
    .split("\n")
    .slice(1)
    .map((e) => e.split(" ").map(Number));
}

function sol() {
    input_data = Input();

    return input_data.sort((a, b) => {
        if (a[1] === b[1]) {
            return a[0] - b[0];
        }

        return a[1] - b[1];
    })
    .map((e) => e.join(" ")).join("\n");
}

console.log(sol());