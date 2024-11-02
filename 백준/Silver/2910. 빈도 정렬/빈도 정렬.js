const [in1, in2] = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const [arrLen, uniqueNum] = in1.split(" ").map(Number);
const data = in2.split(" ").map(Number);
const obj = {};
const uniqueArr = [];

for (let el of data) {
    if (obj[el]) {
        obj[el]++;
    } else {
        obj[el] = 1;
        uniqueArr.push(el);
    }
}

data.sort((a, b) => {
    if (obj[a] < obj[b]) return 1;
    else if (obj[a] === obj[b]) return uniqueArr.indexOf(a) < uniqueArr.indexOf(b) ? -1 : 1;
    else return -1;
});

console.log(data.join(" "));