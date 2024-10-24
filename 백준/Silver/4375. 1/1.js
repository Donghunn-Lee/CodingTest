const fs = require('fs');
const input = fs.readFileSync("./dev/stdin").toString().trim().split('\n').map(Number);
let answer = []

for(let i = 0; i<input.length; i++){
  let  gun= input[i];
  let target = gun;
  let cnt = 0;
  while(true){
    if(target==0){
      answer.push(cnt)
      break;
    }else if(target%10==1){
      cnt++;
      target = Math.floor(target/10)
    }else{
      target+=gun
    }
  }
}
console.log(answer.join('\n'))