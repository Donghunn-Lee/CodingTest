//  피보나치 비스무리한 수열

const fs = require("fs");
const N = +fs.readFileSync(process.platform == "linux" ? "/dev/stdin" : 'input.txt').toString().trim()

function sol() {
    const fivonichi = Array(N + 1);
    fivonichi[1] = BigInt(1);
    fivonichi[2] = BigInt(1);
    fivonichi[3] = BigInt(1);

    for (let i = 4; i <= N; i++) {
        fivonichi[i] = (fivonichi[i - 1] + fivonichi[i - 3]);
    }

    console.log(fivonichi[N].toString());
}

sol();