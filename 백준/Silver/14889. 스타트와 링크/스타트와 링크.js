// 스타트와 링크

// N <= 20이므로 완전 탐색으로 모든 조합을 구해야겠다고 생각함.
// 한 팀의 인원이 N / 2가 될 때까지 재귀를 반복하면 그 시점에서 다른 팀의 명수도 N / 2이 됨.
// 이 때의 팀을 기준으로 시너지를 계산, 두 팀의 시너지 차의 최솟값을 갱신함.

const fs = require("fs");
const input = fs.readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt").toString().trim().split("\n");

// 변수 선언부
const N = +input[0];  // N은 사람의 수
const synergy = input.slice(1).map(e => e.split(" ").map(Number));  // 시너지 값을 2차원 배열로 변환
let minDifference = Infinity;  // 시너지 차이의 최소값을 저장하기 위한 변수, 초기값은 무한대

// 팀 시너지 합 계산 함수
// 주어진 팀 배열을 받아 해당 팀의 시너지 합을 계산하는 함수
function calSynergy(team) {
    let totalScore = 0;  // 팀의 시너지 총합
    const teamSize = team.length;  // 팀의 크기
    
    // 이중 for문을 통해 팀 내의 모든 쌍에 대해 시너지 값을 합산
    for (let i = 0; i < teamSize; i++) {
        for (let j = i + 1; j < teamSize; j++) {
            // 팀 내 두 사람의 시너지를 서로 더해줌 (대칭적이기 때문에 두 값을 더함)
            totalScore += synergy[team[i]][team[j]] + synergy[team[j]][team[i]];
        }
    }
    
    return totalScore;  // 계산된 시너지 총합을 반환
}

// 가능한 모든 조합을 구하며, 팀 간 시너지 차의 최솟값 갱신
// cur: 현재 사람이 속할 인덱스
// team: 현재까지 구성된 팀 배열
function combination(cur, team) {
    // 현재 팀이 N / 2명으로 구성되었다면 다른 팀과의 시너지 차이를 계산
    if (team.length === N / 2) {
        const other = [];  // 현재 팀에 속하지 않은 인원들을 팀으로 구성할 배열
        // 현재 팀에 속하지 않은 사람들을 other 팀으로 구성
        for (let i = 0; i < N; i++) {
            if (!team.includes(i)) {
                other.push(i);
            }
        }
        // 두 팀 간의 시너지 차이를 계산하여 최솟값을 갱신
        const difference = Math.abs(calSynergy(team) - calSynergy(other));
        minDifference = Math.min(minDifference, difference);  // 최솟값 갱신
        return;
    }

    // 현재 인덱스가 범위를 넘어가면 종료
    if (cur === N) return;

    // 현재 인원을 팀에 포함시키는 경우
    team.push(cur);  // 현재 인원을 팀에 추가
    combination(cur + 1, team);  // 다음 인덱스로 재귀 호출

    // 포함시키지 않는 경우
    team.pop();  // 포함시켰던 인원을 다시 제거
    combination(cur + 1, team);
}


function main() {
    combination(0, []);
    console.log(minDifference);
}

main();