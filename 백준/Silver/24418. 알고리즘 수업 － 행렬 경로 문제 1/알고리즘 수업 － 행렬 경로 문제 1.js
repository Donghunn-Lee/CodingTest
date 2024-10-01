const input = require('fs')
	.readFileSync('./dev/stdin')
	.toString()
	.trim()
	.split('\n')
	.map((v) => v.split(' ').map(Number));

const N = input.shift()[0];
let count = 0;
input.unshift(new Array(N).fill(0));

const arr = input.map((v) => [0, ...v]);

function test(arr, n, m) {
	if (n == 0 || m == 0) {
		count++;
		return 0;
	} else return arr[n][m] + Math.max(test(arr, n - 1, m), test(arr, n, m - 1));
}

test(arr, N, N);
console.log(count, N * N);