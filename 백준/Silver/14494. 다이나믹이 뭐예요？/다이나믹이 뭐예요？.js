// 다이나믹이 뭐예요?
const fs = require("fs");
const [N, M] = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "input.txt")
  .toString()
  .trim()
  .split(" ")
  .map(Number);


function main() {
    const arr = Array.from(Array(N + 1), () => Array(M + 1).fill(0));
    
    for (let i = 1; i <= N; i++) {
        arr[i][1] = 1;
    }

    for (let j = 1; j <= M; j++) {
        arr[1][j] = 1;
    }


    for (let i = 2; i <= N; i++) {
        for (let j = 2; j <= M; j++) {
            arr[i][j] = (arr[i - 1][j] + arr[i][j - 1] + arr[i - 1][j - 1]) % 1_000_000_007;
        }
    }

    console.log(arr[N][M]);
}

main();