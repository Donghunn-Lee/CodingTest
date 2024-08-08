// dev/stdin
const fs = require("fs");
let input = fs.readFileSync('dev/stdin').toString().trim().split('\n');

const n = Number(input[0])

let set = new Set()

for(let i = 1; i <= n; i++) {
  const temp = input[i].split(' ')
  if(temp[1].includes('enter')) {
    set.add(temp[0])
  } else {
    set.delete(temp[0])
  }
}
const a = 'a'.toLocaleLowerCase

console.log([...set].sort((a, b) => {
    if (a < b) {
        return 1;
    } else {
        return -1;
    }
}).join('\n'))
