const fs = require("fs");

const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((item) => item.split(" "));

const arr = input.map((item) => item.map((item) => Number(item)));

let numer1 = arr[0][0];
let deno1 = arr[0][1];

let numer2 = arr[1][0];
let deno2 = arr[1][1];

let big = (deno1 > deno2) ? deno1 : deno2;
let small = (deno1 < deno2) ? deno1 : deno2;

let mod = big % small;

while(mod != 0){
    let tmp = mod;
    mod = small % mod;
    small = tmp;
}

let GCD = small;
let LmsOfDeno = deno1 * deno2 / GCD;
numer1 = numer1 * (LmsOfDeno / deno1);
numer2 = numer2 * (LmsOfDeno / deno2);

let numer = numer1 + numer2;

let i = LmsOfDeno;

while(i > 0){
    if(numer == 1 || i == 1){
        break;
    }

    if((numer % i == 0)&&(LmsOfDeno % i == 0)){
        LmsOfDeno = LmsOfDeno / i;
        numer = numer / i;
    }else{
        i--;
    }
}

console.log(numer + " " + LmsOfDeno);