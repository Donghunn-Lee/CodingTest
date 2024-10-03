// 피모나치는 지겨웡~

const fs = require("fs");
const N = +fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "input.txt")
  .toString()
  .trim();

function main() {
    let [tmp_1, tmp_2, tmp_3] = [1, 1, 0];

    if (N < 2) {
        console.log(1);
        return;
    }

    for (let i = 2; i <= N; i++) {
        tmp_3 = (tmp_1 + tmp_2 + 1) % 1_000_000_007;
        [tmp_1, tmp_2] = [tmp_2, tmp_3];
    }

    console.log(tmp_3);
}

main();
