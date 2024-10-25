const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});
let input = [];
rl.on('line', function (line) {
  input.push(line);
})
  .on('close', async function () {
  // 답안 작성
  let answer =0;    
  let n = input[0];
  let m = input[1];
  answer = brute(n,m);
  console.log(answer)
  process.exit();
});

let brute = function(n,m){
  let tmp = [];
  let broke = -1;
  let min = 10001;
  m = m.split(' ');
  for(let i=n-1;i>=0;i--){
    if(min*1<m[i]*1){
      broke = i;
      break;
    }
    tmp.push(m[i]);
    min = m[i]*1;
  }  
  if(broke == -1)return -1;
  for(let i = 0;i<tmp.length;i++){
    if(m[broke]*1>tmp[i]*1){
      let change = tmp.splice(i,1,m[broke]);
      m[broke] = change.join('');
      break;
    }
  }  
  return (m.slice(0,broke+1).join(' ') +' '+ tmp.join(' '));
}