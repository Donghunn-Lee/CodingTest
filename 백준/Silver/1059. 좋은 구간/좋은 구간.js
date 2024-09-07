const [L, S, n] = require('fs').readFileSync('/dev/stdin')
                  .toString().trim().split('\n');
const nums = S.split(" ").map(v => +v).sort((a,b) => a-b);

const findAns = () => {
  // 만약 n이 집합에 포함되는 수라면 0을 출력.
  if(nums.find(num => num === +n)) return 0;

  let minVal = 0; // n보다 작은 수를 담아둘 변수.
  let maxVal = 0; // n보다 큰 수를 담아둘 변수.

  // n이 포함된 구간을 찾아야하기 때문에 n보다 작은 수를 구하고, n보다 첫번째 큰 수를 구해야함.
  nums.forEach(num => {
    if(num < n) minVal = num; 
    else if(num > n && maxVal === 0) maxVal = num;
  })

  // 집합에 있는 값은 포함하지 않으므로 작은 값은 1을 더하고, 큰 값은 1을 빼줌.
  maxVal -= 1
  minVal += 1

  return ((n-minVal) * (maxVal-n+1) + (maxVal-n)) // 공식 적용해서 돌려주기.
}

console.log(findAns())