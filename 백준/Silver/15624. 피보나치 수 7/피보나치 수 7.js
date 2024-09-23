//  피보나치 수 7

const fs = require("fs");
const N = +fs.readFileSync(process.platform == "linux" ? "/dev/stdin" : 'input.txt').toString().trim()

function sol() {
    const fivonichi = Array(N + 1);
    fivonichi[0] = 0;
    fivonichi[1] = 1;

    for (let i = 2; i <= N; i++) {
        fivonichi[i] = (fivonichi[i - 1] + fivonichi[i - 2]) % 1_000_000_007;
    }

    console.log(fivonichi[N]);
}

sol();