const [in1, in2] = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const [N, X] = in1.split(" ").map(Number);
const arr = in2.split(" ").map(Number);

const maxSubarraySum = (arr, num) => {
  if (arr.reduce((acc, cur) => acc + cur, 0) === 0) return "SAD";
  const obj = {};
  let maxSum = 0;
  let tempSum = 0;
  let subNum = 1;
  for (let i = 0; i < num; i++) {
    maxSum += arr[i]; // 우선 첫 번째 합을 maxSum에 저장
  }
  tempSum = maxSum;
  for (let i = num; i < arr.length; i++) {
    // arr[0] 빼고 arr[num] 더하면 새로운 window.
    // 이것을 반복
    tempSum = tempSum - arr[i - num] + arr[i];
    if (maxSum === tempSum) subNum++;
    else if (maxSum < tempSum) {
      maxSum = tempSum;
      subNum = 1;
    }
  }
  return maxSum + "\n" + subNum;
};

console.log(maxSubarraySum(arr, X));