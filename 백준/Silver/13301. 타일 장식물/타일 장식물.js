// 타일 장식물

function dp(n) {
    const dp_table = Array(n + 1).fill(BigInt(0));
    dp_table[1] = BigInt(1);
    dp_table[2] = BigInt(1);

    if (n === 1) {
        return 4;
    }

    for (let i = 3; i <= n; i++) {
        dp_table[i] = dp_table[i - 1] + dp_table[i - 2];
    }

    return dp_table[n] * BigInt(4) + dp_table[n - 1] * BigInt(2);
}

function main() {
    const fs = require('fs');
    const N = +fs.readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt").toString().trim();

    console.log(dp(N).toString());
}

main();