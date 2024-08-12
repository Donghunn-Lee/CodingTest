const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];
// deque
const snakeBody = [[0, 0]];
// 상우하좌 (시계방향)
const dy = [-1, 0, 1, 0];
const dx = [0, 1, 0, -1];

// 컨트롤러 변수
let currentDirection = 1; // 기본값 우방향
let seconds = 0;
let isApple;
let collision = false;

// L or D를 받아서 전역 현재 방향 변수를 0 1 2 3 중 하나로 한 칸 바꿈
const turn = (LD) => {
  if (LD === "L")
    currentDirection = currentDirection ? currentDirection - 1 : 3;
  if (LD === "D")
    currentDirection = currentDirection === 3 ? 0 : currentDirection + 1;
};

rl.on("line", (line) => {
  input.push(line);
}).on("close", () => {
  const N = +input[0];
  const appleNum = +input[1];
  let applePosList = input
    .slice(2, 2 + appleNum)
    .map((el) => el.split(" ").map(Number));
  const directionNum = +input[appleNum + 2];
  const directionList = input.slice(appleNum + 3).map((el) => {
    const directionInfo = el.split(" ");
    return [+directionInfo[0], directionInfo[1]];
  });
  while (true) {
    isApple = false;
    const newY = snakeBody[0][0] + dy[currentDirection];
    const newX = snakeBody[0][1] + dx[currentDirection];
    // 벽 충돌 검사
    if (newY < 0 || newY >= N || newX < 0 || newX >= N) break;
    // 몸체 충돌 검사
    snakeBody.forEach((body) => {
      if (body[0] === newY && body[1] === newX) {
        collision = true;
      }
    });
    if (collision) break;
    // 사과 검사
    // 사과인 경우 pop X, unshift O
    applePosList.forEach((applePos, idx) => {
      if (applePos[0] - 1 === newY && applePos[1] - 1 === newX) {
        applePosList.splice(idx, 1);
        snakeBody.unshift([newY, newX]);
        isApple = true;
      }
    });
    // 사과가 아닌 경우 pop O
    if (!isApple) {
      snakeBody.unshift([newY, newX]);
      snakeBody.pop();
    }
    seconds++;
    // 방향 전환
    if (directionList.length && seconds === directionList[0][0]) {
      turn(directionList[0][1]);
      directionList.shift();
    }
  }
  console.log(seconds + 1);
});