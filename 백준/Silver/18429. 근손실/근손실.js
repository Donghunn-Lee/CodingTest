const [n, k, ...arr] = require("fs").readFileSync("/dev/stdin").toString().trim().split(/\s/);
const N = Number(n);
const K = Number(k);
const kit = arr.map(Number);

let visit = Array.from({length: N}, _ => false);
let result = 0;

function dfs(day, weight){
    if(weight < 0) {
        return;
    }
    
    if(day === N) {
        result = result + 1;
        return;
    }
    
    for(let i = 0; i < N; i++){
        if (visit[i] === true) continue;
        visit[i] = true;
        dfs(day + 1, weight + kit[i] - K);
        visit[i] = false;
    }
}

dfs(0, 0);
console.log(result);