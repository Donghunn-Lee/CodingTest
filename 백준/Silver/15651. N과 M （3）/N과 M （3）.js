// N과 M (3)

const fs = require("fs");
const [N, M] = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "input.txt")
  .toString()
  .trim()
  .split(" ")
  .map(Number);

function main() {
    const allSeq = [];
    const seq = [];

    const recursion = (count) => {
        if (count === M) {
            allSeq.push([...seq].map((e) => e.toString()).join(" "));
            seq.pop();
            return;
        }

        for (let i = 1; i <= N; i++) {
            seq.push(i);
            recursion(count + 1);
        }
        seq.pop();
    }

    recursion(0);

    console.log(allSeq.join("\n"));
}

main();