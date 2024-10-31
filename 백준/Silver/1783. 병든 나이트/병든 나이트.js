const readFileSyncAddress = "/dev/stdin";

let input = require("fs")
  .readFileSync(readFileSyncAddress)
  .toString()
  .trim()
  .split(" ")
  .map(Number);

const [h, w] = input;
// 1. 칸이 넉넉한 경우
// 4가지 이동을 모두 사용해야 하기에 w - 2
if (w >= 7 && h >= 3) {
  console.log(w - 2);
}
// 2. 높이는 충분하지만 너비가 애매한 경우 (1)
// 4가지 이동을 모두 사용하지 못하며 최대 4번까지 이동 가능
else if ((w === 6 || w === 5) && h >= 3) {
  console.log(4);
}
// 3. 높이는 충분하지만 너비가 애매한 경우 (2)
// 4가지 이동을 모두 못하며 너비도 매우 작은 경우
else if (w <= 4 && h >= 3) {
  console.log(w);
}
// 4. 높이가 1인 경우 이동 불가 => 출력 1
else if (h === 1) {
  console.log(1);
}
// 5. 높이가 작고 너비가 충분한 경우
// 최대 이동 횟수는 4
else if (h === 2 && w >= 3) {
  const calced = Math.floor((w + 1) / 2);
  console.log(calced > 4 ? 4 : calced);
}
// 6. 예외 케이스
// 2 * 2인 경우 등 이동 불가
else {
  console.log(1);
}