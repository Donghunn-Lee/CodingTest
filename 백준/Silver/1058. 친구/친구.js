// 친구

const fs = require("fs");
const input = fs.readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt").toString().trim().split("\n");

const N = +input.shift();
const relationship = input.map(e => e.split(""));
let max = 0;

relationship.forEach((arr,i)=>{
    const temp = [];
    arr.forEach((val,index)=>{
        if(val==='Y')
            temp.push(index);
    });
    let list = new Set(temp);
    temp.forEach(v=>{
        relationship[v].forEach((str,ind)=>{
            if(str==='Y')
                list.add(ind);
        });
    })
    list.delete(i);
    let count = list.size;
    if(max<count)
        max = count;
})

console.log(max);