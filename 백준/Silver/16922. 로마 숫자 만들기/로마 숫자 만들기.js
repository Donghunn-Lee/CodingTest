const fs = require('fs');
const input = fs.readFileSync("./dev/stdin").toString().trim();
const N = +input

const Rome = [1,5,10,50];

let cnt = 1;
let answer = [1,5,10,50];
while(cnt<N){
  let temp = [];
  Rome.forEach(v=>{
    for(let i  = 0; i<answer.length; i++){
      temp.push(answer[i]+v)
    }
  })
  answer = [...new Set(temp)];
  cnt++;
}

console.log(answer.length)