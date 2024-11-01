const fs = require('fs');
const URI = process.platform ==='linux'? 'dev/stdin':'./19941.txt';
const inputs = fs.readFileSync(URI).toString().trim().split('\n');
let [N,K] = inputs[0].split(' ');
const target = inputs[1];
N = Number(N);
K = Number(K);
const peopleArray = new Array();
const hambergerArray = new Array();
for (let i = 0; i < N; i++){
    if (target[i] === 'H') hambergerArray.push(i)
    else peopleArray.push(i);
}
let [peopleIdx,hambergerIdx,ans] = [0,0,0];
while (peopleIdx < peopleArray.length && hambergerIdx < hambergerArray.length){
    const peoplePosition = peopleArray[peopleIdx];
    const hambergerPosition = hambergerArray[hambergerIdx];
    if (peoplePosition-K <= hambergerPosition && peoplePosition+K >= hambergerPosition){
        ans ++;
        peopleIdx ++;
        hambergerIdx ++;
    } else if (peoplePosition-K > hambergerPosition) hambergerIdx ++;
    else peopleIdx ++;
}
console.log(ans)