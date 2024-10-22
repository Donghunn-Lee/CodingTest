const [N, ...input] = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n');

function sumOfNumbers(input) {
  const numbers = input.match(/\d/g);
  const sum = numbers?.reduce((acc, num) => acc + parseInt(num, 10), 0) || 0;
  return sum;
}

const sortedInput = input.sort(
  (a, b) =>
    a.length - b.length ||
    sumOfNumbers(a) - sumOfNumbers(b) ||
    a.localeCompare(b),
);

console.log(sortedInput.join('\n'));