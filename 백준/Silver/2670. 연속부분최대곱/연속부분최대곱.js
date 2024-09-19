// 연속부분최대곱

const fs = require("fs");
const input = fs.readFileSync(process.platform == "linux" ? "/dev/stdin" : 'input.txt').toString().trim().split("\n");

function main() {    
    const N = +input.shift();
    const seq = input.map(Number);
    let max = 0;
    let tmp = seq[0];

    for (let i = 1; i < N; i++) {
        if (seq[i] > tmp * seq[i]) tmp = seq[i];
        else tmp *= seq[i]
        max = Math.max(max, tmp);
    }

    console.log(max.toFixed(3));
}

main();