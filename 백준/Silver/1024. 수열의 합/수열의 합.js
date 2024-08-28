const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('', (input) => {
    const [N, L] = input.split(' ').map(Number);

    let x = -1;
    let t = -1;
    let len = -1;

    for (let i = L; i <= 100; i++) {
        t = (i - 1) * i / 2;
        if ((N - t) % i === 0) {
            x = (N - t) / i;
            len = i;
            break;
        }
    }

    if (x < 0) {
        console.log(-1);
    } else {
        let result = '';
        for (let i = 0; i < len; i++) {
            result += (x + i) + ' ';
        }
        console.log(result.trim());
    }

    rl.close();
});