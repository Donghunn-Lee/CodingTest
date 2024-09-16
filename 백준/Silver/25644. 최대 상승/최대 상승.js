// 최대 상승

function sol(n, data) {
    let cur = data[0];
    let revenue = 0;

    for (let i = 1; i < n; i++) {
        if (data[i] < cur) {
            cur = data[i];
        } else {
            revenue = Math.max(revenue, data[i] - cur);
        }
    }

    return revenue;
}

function main() {
    const fs = require("fs");
    const input = fs.readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt").toString().trim().split("\n");
    const N = +input.shift();
    const stocks_data = input[0].split(" ").map(Number);

    console.log(sol(N, stocks_data));
}

main();
