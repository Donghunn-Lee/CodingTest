// 로봇 청소기

const fs = require("fs");
const input = fs.readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt").toString().trim().split("\n");

// 변수 선언.
const [N, M] = input[0].split(" ").map(Number);
const [r, c, d] = input[1].split(" ").map(Number);
const room = input.slice(2, 2 + N).map(e => e.split(" ").map(Number));
const direction = [[-1, 0], [0, 1], [1, 0], [0, -1]];

function sol() {
    // 현재 좌표, 방향 설정.
    let [ci, cj, cd] = [r, c, d];
    let count = 0;
    
    // 로봇 청소기가 더 이상 작동할 수 없을 때까지 반복.
    while(true) {
        
        // 현재 칸이 청소되어 있지 않다면 청소. 청소한 칸의 값을 2로 할당.
        if (room[ci][cj] === 0) {
            room[ci][cj] = 2;
            count++;
        }

        // 주변 4칸 중 청소되지 않은 칸이 있는지 여부를 bool값으로 판별.
        let flag = false;

        for (let i = 1; i <= 4; i++) {
            // 방향값에 1씩 빼가며 반시계방향 90도 전환.
            let nd = (4 + cd - i) % 4;
            let [ni, nj] = [ci + direction[nd][0], cj + direction[nd][1]];

            // 방향을 전환해 확인한 칸이 벽이 아닌지, 이미 청소가 안 된 칸이 맞는지를 확인.
            // 벽이거나 청소가 된 칸이라면 continue로 다음 방향을 확인.
            if (ni < 0 || N <= ni || nj < 0 || M <= nj || room[ni][nj] !== 0) continue;

            // 위 if문이 실행되지 않았다면 현재 방향의 칸은 청소가 되지 않은 칸임.
            // flag에 true를 할당, 로봇 청소기기의 위치를 해당 칸으로 이동하고 반복 종료.
            ci = ni, cj = nj, cd = nd;
            flag = true;
            break;
        }

        // 주변 4칸 중 청소되지 않은 칸을 찾았다면 아래 코드를 실행하지 않고 다음 반복을 위해 continue.
        if (flag) continue;

        // 청소되지 않은 칸이 없었을 경우, 한 칸 후진해야함. 후진한 칸의 좌표를 선언.
        let [bi, bj] = [ci - direction[cd][0], cj - [direction[cd][1]]];

        // 후진한 칸이 벽이라면 작동 종료.
        if (bi < 0 || N <= bi || bj < 0 || M <= bj || room[bi][bj] === 1) break;

        // 벽이 아니라면 로봇 청소기를 1칸 후진하여 다시 반복.
        ci = bi, cj = bj;
    }
    
    // 로봇 청소기가 작동을 종료하여 반복이 종료된 경우, 청소한 칸의 개수인 count를 반환.
    return count;
}

console.log(sol());