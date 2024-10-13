const solve = (N, M, arr) => {
  const permutation = [];
  const output = [];
  const recursion = () => {
    if (permutation.length === M) {
      output.push(permutation.join(' '));
    } else {
      for (const i of arr) {
        permutation.push(i);
        recursion();
        permutation.pop();
      }
    }
  };

  recursion();
  console.log(output.join('\n'));
};

const [N, M, ...arr] = require('fs').readFileSync('/dev/stdin').toString().trim().split(/\s+/).map(v => +v);
arr.sort((a, b) => a - b);
solve(N, M, arr);