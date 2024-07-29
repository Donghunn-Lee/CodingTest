// 부녀회장이 될테야

const fs = require("fs");

function Input() {
    return fs.readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
    .toString()
    .split("\n")
    .map(Number);
}

function sol() {
    let input_data = Input();
    let T = input_data.shift();
    let ans = [];

    for (let t = 0; t < T; t++) {
        let k = input_data[t * 2], n = input_data[t * 2 + 1];
        let apartment = Array(Array(n).fill(0).map((v, idx) => idx + 1));
        
        for (let i = 1; i < k + 1; i++) {
            let cur_floor = [1];

            for (let j = 1; j < n; j++) {
                cur_floor.push(cur_floor[j - 1] + apartment[i - 1][j])
            }

            apartment.push(cur_floor);
        }

        ans.push(apartment[k][n - 1]);
    }

    console.log(ans.join("\n"));
}

sol();