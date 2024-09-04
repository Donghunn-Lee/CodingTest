// 명령 프롬프트

const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split("\n");

const N = +input.shift();
const files = input;

let pattern = '';
let length = files[0].length;

function sol() {
    for (let i = 0; i < length; i++) {
        let cur = files[0][i];
        let flag = true;

        for (let j = 1; j < N; j++) {
            if (files[j][i] !== cur) {
                pattern += '?'
                flag = false;
                break;
            }
        }
    
        if (flag) {
            pattern += cur;
        }
    
    }

    return pattern;
}


console.log(sol());