const [[T], arr] = require('fs')
	.readFileSync('./dev/stdin')
	.toString()
	.trim()
	.split('\n')
	.map((v) => v.split(' ').map(Number));

const answer = [0];
let min = arr[0];
for (let i = 1; i < T; i++) {
	const max = arr[i] - min < answer[i - 1] ? answer[i - 1] : arr[i] - min;
	answer.push(max);
	min = min > arr[i] ? arr[i] : min;
}

console.log(answer.join(' '));