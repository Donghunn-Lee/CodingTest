// 어린왕자

const fs = require("fs");
const input = fs.readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt").toString().trim().split("\n").map(e => e.split(" ").map(Number));

function sol(sx, sy, tx, ty, planets) {
    let count = 0;

    for (const planet of planets) {
        let [cx, cy, r] = planet;

        if ((sx-cx)**2 + (sy-cy)**2 < r**2) count++;
        if ((tx-cx)**2 + (ty-cy)**2 < r**2) count++;
        if ((sx-cx)**2 + (sy-cy)**2 < r**2 && (tx-cx)**2 + (ty-cy)**2 < r**2) count -= 2;
    }

    return count;
}

function main() {
    const N = input[0];
    let cur = 1;
    const answer = [];

    for (let i = 0; i < N; i++) {
        const [x1, y1, x2, y2] = input[cur++];
        const n = input[cur++];
        const planets = [];

        for (let j = 0; j < n; j++) {
            planets.push(input[cur++]);
        }

        answer.push(sol(x1, y1, x2, y2, planets))
    }

    console.log(answer.join("\n"));
}

main();