const len = require('fs').readFileSync('/dev/stdin').toString() * 1;

let prevN = 1, n = 0;

for (let i = 0; i < len; i++) {
    const tmpPrevN = BigInt(n);

    n = tmpPrevN + BigInt(prevN);

    prevN = tmpPrevN;
}

console.log(n.toString());