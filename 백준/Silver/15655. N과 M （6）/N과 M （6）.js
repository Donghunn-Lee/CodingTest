const solve = (N, M, arr) => {
	let permutation = [];
	const chosen = new Array(N).fill(false);
	const output = [];
	const recursion = prev => {
		if (permutation.length === M) {
			output.push(permutation.join(' '));
		} else {
			chosen.forEach((bool, i) => {
				if (!bool && i > prev) {
					chosen[i] = true;
					permutation.push(arr[i]);
					recursion(i);
					chosen[i] = false;
					permutation.pop();
				}
			});
		}
	};

	recursion(-1);
	console.log(output.join('\n'));
};

const [N, M, ...arr] = require('fs').readFileSync('/dev/stdin').toString().trim().split(/\s+/).map(v => +v);
arr.sort((a, b) => a - b);
solve(N, M, arr);