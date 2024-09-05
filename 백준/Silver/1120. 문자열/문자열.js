// 문자열

const fs = require('fs');
const [A, B] = fs.readFileSync('/dev/stdin').toString().trim().split(" ");

let count = 0;

for (let i = 0; i <= B.length - A.length; i++) {
    let tmp = 0;

    for (let j = 0; j < A.length; j++) {
        if (A[j] === B[j + i]) {
            tmp++;
        }
    }

    count = Math.max(count, tmp);
}

console.log(A.length - count)