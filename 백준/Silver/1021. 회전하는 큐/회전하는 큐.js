// 회전하는 큐

const fs = require("fs");
const input = fs.readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt").toString().trim().split("\n").map(e => e.split(" ").map(Number));

function sol(arr, target) {
    let count = 0;

    for (let i = 0; i < target.length; i++) {
        let idx = arr.indexOf(target[i]);
        let [left, right] = [idx, arr.length - idx];

        right = arr.length - idx;

        if (left <= right) {
            for (let j = 0; j < idx; j++) {
                arr.push(arr.shift());
                count++;
            }

            arr.shift();

        } else if (left > right) {
            for (let j = arr.length - 1; idx <= j; j--) {
                arr.unshift(arr.pop());
                count++;
            }

            arr.shift();
        }
    }

    return count;
}

function main() {
    const [N, M] = input[0];
    const target = input[1];
    const arr = Array(N).fill(0);
    target.forEach((val) => arr[val - 1] = val)
    
    console.log(sol(arr, target));
}

main();

