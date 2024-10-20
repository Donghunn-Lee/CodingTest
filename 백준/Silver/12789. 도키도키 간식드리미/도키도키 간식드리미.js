// 도키도키 간식드리미

const filePath = process.platform === 'linux' ? '/dev/stdin' : 'input.txt';
const input = require('fs')
  .readFileSync(filePath)
  .toString()
  .trim()
  .split('\n');

const N = +input.shift();
const queue = input[0].split(" ").map(Number);

function main() {
    const secondQueue = [];
    let currentNumber = 1;

    while (0 < queue.length + secondQueue.length) {
        if (queue[0] === currentNumber) {
            queue.shift();
            currentNumber++;
        } else if (secondQueue.at(-1) === currentNumber) {
            secondQueue.pop();
            currentNumber++;
        } else {
            if (queue.length === 0) {
                console.log('Sad');
                return
            }
            secondQueue.push(queue.shift());
        }
    }

    if (currentNumber - 1 === N) {
        console.log('Nice');
    } else {
        console.log('Sad');
    }
}

main();