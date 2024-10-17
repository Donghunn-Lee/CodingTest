// 포닉스의 문단속

// 친구가 괜찮다고 추천해줘서 풀어 본 문제.
// 확실히 최근 문제라 그런지 조금 신선한 느낌이 있었던 것 같음.
// 보자마자 그리디 알고리즘임을 파악.
// 왼쪽부터 문자를 탐색하며 남은 K번으로 이 문자를 A로 만들 수 있는지를 계속해서 체크. 가능하면 변환.
// 모든 문자를 탐색하고 K가 0 이상인 경우, 사전 순으로 가장 작아야 하므로 마지막 문자를 K번 더 돌림.

// + 이미 문자가 A일 때 돌릴 필요가 없다는 것과, 마지막에 남은 K가 26보다 큰 경우 K를 버리는 게 아니라 남은 횟수만큼 더 돌려야 한다는 점을 생각하지 못함. 떠올려서 남은 K를 26으로 mod연산함.
const filePath = process.platform === 'linux' ? '/dev/stdin' : 'input.txt';
const input = require('fs')
  .readFileSync(filePath)
  .toString()
  .trim()
  .split('\n');

const ALPHA_LENGTH = 90;
let [N, K] = input.shift().split(' ').map(Number);
const S = [...input[0]];

function main() {
  for (let i = 0; i < N; i++) {
    const asciiCode = S[i].charCodeAt();
    if (S[i] !== 'A' && ALPHA_LENGTH < asciiCode + K) {
      S[i] = 'A';
      K = asciiCode + K - ALPHA_LENGTH - 1;
    }
  }

  if (0 < K) {
    S[N - 1] = String.fromCharCode(S[N - 1].charCodeAt() + K % 26);
  }

  console.log(S.join(''));
}

main();
