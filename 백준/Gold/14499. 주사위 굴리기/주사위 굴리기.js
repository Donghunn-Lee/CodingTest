const fs = require("fs");
const input = fs.readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt").toString().trim().split("\n");

const [N, M, x, y, K] = input[0].split(" ").map(Number);
const graph = [];
for (let i = 1; i <= N; i++) {
    graph.push(input[i].split(" ").map(Number));
}
const cmds = input.at(-1).split(" ").map(Number);
const dice = {
    top : 0,
    bottom : 0,
    left : 0,
    right : 0,
    front : 0,
    back : 0,
};
const direction = {
    1 : [0, 1],   // 동쪽
    2 : [0, -1],  // 서쪽
    3 : [-1, 0],  // 북쪽
    4 : [1, 0]    // 남쪽
}

function roleDice(dir) {
    let tmp = 0;

    if (dir === 1) { // 동쪽
        tmp = dice.top;
        dice.top = dice.left;
        dice.left = dice.bottom;
        dice.bottom = dice.right;
        dice.right = tmp;

    } else if (dir === 2) { // 서쪽
        tmp = dice.top;
        dice.top = dice.right;
        dice.right = dice.bottom;
        dice.bottom = dice.left;
        dice.left = tmp;
    } else if (dir === 3) { // 북쪽
        tmp = dice.top;
        dice.top = dice.back;
        dice.back = dice.bottom;
        dice.bottom = dice.front;
        dice.front = tmp;
    } else if (dir === 4) { // 남쪽
        tmp = dice.top;
        dice.top = dice.front;
        dice.front = dice.bottom;
        dice.bottom = dice.back;
        dice.back = tmp;
    }
}

function sol() {
    const answer = [];
    let ci = x, cj = y;  // 초기 좌표 설정

    for (const cmd of cmds) {
        const dir = direction[cmd];
        const ni = ci + dir[0], nj = cj + dir[1];

        if (ni < 0 || ni >= N || nj < 0 || nj >= M) continue;  // 범위 밖으로 나가면 무시
        ci = ni, cj = nj;

        roleDice(cmd);
        answer.push(dice.top);

        if (graph[ci][cj] === 0) {
            graph[ci][cj] = dice.bottom;
        } else {
            dice.bottom = graph[ci][cj];
            graph[ci][cj] = 0;
        }
    }

    return answer.join("\n");
}

console.log(sol());
