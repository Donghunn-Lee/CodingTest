const fs = require("fs");

const input = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `1 1`
).split(" ");

const date = new Date(`2007-${input[0]}-${input[1]}`);

// solution 1
const day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"];

// solution 2
console.log(date.toString().slice(0, 3).toUpperCase());
