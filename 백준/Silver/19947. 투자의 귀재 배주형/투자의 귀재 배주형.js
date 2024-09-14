const [H, Y] = require('fs').readFileSync('./dev/stdin').toString().trim().split(' ').map(Number);

let dp = Array(Y + 1).fill(0);

dp[0] = H;
const bokni = [null, 1.05, null, 1.2, null, 1.35];

for (let i = 1; i <= Y; i++) {
	for (let j = 1; j <= 5; j += 2) {
		if (i - j >= 0) dp[i] = Math.max(dp[i], Math.floor(dp[i - j] * bokni[j]));
	}
}

console.log(dp[Y]);