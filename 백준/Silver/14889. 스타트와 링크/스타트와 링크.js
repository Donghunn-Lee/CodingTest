// 스타트와 링크

// N <= 20이므로 완전 탐색으로 모든 조합을 구해야겠다고 생각함.
// 한 팀의 인원이 N / 2가 될 때까지 재귀를 반복하면 그 시점에서 다른 팀의 명수도 N / 2이 됨.
// 이 때의 팀을 기준으로 시너지를 계산, 두 팀의 시너지 차의 최솟값을 갱신함.

const fs = require("fs");
const input = fs.readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt").toString().trim().split("\n");

// 변수 선언부
const N = +input[0];
const synergy = input.slice(1).map(e => e.split(" ").map(Number));
const allMembers = new Set();       // Start를 기준으로 팀을 만들고, 차집합으로 나머지 멤버를 구하기 위한 전체 집합.
for (let i = 0; i < N; i++) allMembers.add(i);

let Start = new Set();  // 팀을 만들 기준 집합.
let Link = new Set();   // Link는 Start에 들지 않은 다른 인원을 담게 됨.
let minDifference = Infinity;

// 팀 시너지 합 계산.
function calSynergy (team) {
    let totalScore = 0;

    for (let i of team) {
        for (let j of team) {
            if (i == j) continue;

            totalScore += synergy[i][j];
        }
    }

    return totalScore;
}

// 가능한 모든 조합을 구하며, 팀간 시너지 차의 최솟값을 갱신.
function combination(cur, n) {
    // Start에 N / 2명이 들어갔다면 이미 두 팀이 구해진 것이므로 시너지를 계산해 갱신 후 리턴.
    if (n === N / 2) {
        Link = [...allMembers].filter(e => !Start.has(e));
        minDifference = Math.min(minDifference, Math.abs(calSynergy(Start) - calSynergy(Link)));
        return;
    }

    // 만약 이미 N / 2명을 Start에 담지 않고 넘어갔다면, 남은 인원은 모두 Start에 담아야 N / 2명을 만들 수 있음.
    // 때문에 조건을 만족하면 현재 인원부턴 모두 Start에 담으며 재귀를 진행.
    if (N / 2 === cur - n) {
        Start.add(cur);
        combination(cur + 1, n + 1);

        Start.delete(cur);
        return;
    }

    // 현재 인원을 Start에 담는 경우, 집합에 추가.
    // 현재 인원 번호인 cur과 Start에 담은 인원 수인 n을 모두 증가시켜 함수 실행.
    Start.add(cur);
    combination(cur + 1, n + 1);

    // 담지 않은 경우를 계산하기 위해 이미 담은 인원을 제거 후 n이 아닌 cur만 늘려서 함수 진행.
    Start.delete(cur);
    combination(cur + 1, n);
}

function main() {
    combination(0, 0, 0);

    console.log(minDifference);
}

main();