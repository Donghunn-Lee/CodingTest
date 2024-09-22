// 점화식

const fs = require("fs");
const N = +fs.readFileSync(process.platform == "linux" ? "/dev/stdin" : 'input.txt').toString().trim()

function sol() {
    const seq = Array(N + 1).fill(BigInt(0));
    seq[0] = BigInt(1);
    seq[1] = BigInt(1);

    for (let i = 2; i <= N; i++) {
        for (let j = 0; j < i; j++) {
            seq[i] += seq[j] * seq[i - j - 1];
        }
    }

    return seq[N].toString();
}

console.log(sol());