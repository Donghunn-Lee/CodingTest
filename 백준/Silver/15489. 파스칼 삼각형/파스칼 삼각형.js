const [R, C, W] = require('fs').readFileSync('./dev/stdin').toString().trim().split(' ').map(Number);
const dp = [[1], [1, 1]];
const N = R + W - 2;

for (let i = 2; i <= N; i++) {
	dp[i] = [];
	dp[i][0] = 1;
	for (let j = 1; j < i; j++) {
		dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
	}
	dp[i][i] = 1;
}
let r = R - 1;
let c = C - 1;
let answer = 0;
for (let i = 1; i <= W; i++) {
	for (let j = 0; j < i; j++) {
		answer += dp[r][c + j];
	}
	r++;
}

console.log(answer);