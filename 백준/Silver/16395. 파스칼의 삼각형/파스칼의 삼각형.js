// 파스칼의 삼각형

function sol () {
    const fs = require("fs");
    const [n, k] = fs.readFileSync(process.platform === "linux" ? "/dev/stdin" : "input.txt").toString().trim().split(" ").map(Number);
    const triangle = Array(n).fill(0).map((_, idx) => {
        const arr = Array(idx + 1);
        arr[0] = 1;
        arr[idx] = 1;
        return arr;
    });

    for (let i = 2; i < n; i++) {
        for (let j = 1; j < i; j++) {
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j];
        }
    }

    console.log(triangle[n - 1][k - 1]);
}

sol();
