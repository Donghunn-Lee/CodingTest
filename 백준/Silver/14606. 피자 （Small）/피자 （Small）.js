// 피자 (Small)

function divide(n, nxt_table) {
    let [a, b] = [Math.floor(n / 2), Math.ceil(n / 2)];
    nxt_table.push(a);
    nxt_table.push(b);
    
    return a * b;
}

function main() {
    const fs = require("fs");
    const N = +fs.readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt").toString().trim();
    let table = [N];
    let pleasure = 0;

    while (table.length !== N) {
        const nxt_table = [];

        for (let i = 0; i < table.length; i++) {
            if (table[i] == 1) {
                nxt_table.push(1);
            } else {
                pleasure += divide(table[i], nxt_table);
            }
        }

        table = nxt_table
    }

    console.log(pleasure);
}

main();