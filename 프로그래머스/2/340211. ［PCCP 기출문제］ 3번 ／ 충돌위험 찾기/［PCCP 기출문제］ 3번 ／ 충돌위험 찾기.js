function solution(points, routes) {
  let result = 0;
  const robot_path = [];

  // 정답 코드와 같은 방식으로 한 칸씩 이동하는 함수
  const getNextPosition = (r, c, targetR, targetC) => {
    if (r !== targetR) return r > targetR ? [r - 1, c] : [r + 1, c];
    if (c !== targetC) return c > targetC ? [r, c - 1] : [r, c + 1];
    return [r, c];
  };

  // 각 로봇의 경로 계산
  routes.forEach((route) => {
    let startPoint = route.shift();
    let history = [points[startPoint - 1]];

    while (route.length) {
      let [nowR, nowC] = history.at(-1);
      let [targetR, targetC] = points[route[0] - 1];

      let [nextR, nextC] = getNextPosition(nowR, nowC, targetR, targetC);

      history.push([nextR, nextC]);
      if (nextR === targetR && nextC === targetC) {
        route.shift();
      }
    }

    robot_path.push(history);
  });

  const max_length = Math.max(...robot_path.map((v, i) => v.length));

  // 정답 코드와 같은 충돌 검사 방식
  for (let i = 0; i < max_length; i++) {
    let crushPoints = [];
    
    for (let j = 0; j < robot_path.length - 1; j++) {
      for (let k = j + 1; k < robot_path.length; k++) {
        if (
          robot_path[j][i] && robot_path[k][i] &&
          robot_path[j][i][0] === robot_path[k][i][0] &&
          robot_path[j][i][1] === robot_path[k][i][1]
        ) {
          let alreadyInclude = crushPoints.some(
            (point) => point[0] === robot_path[j][i][0] && point[1] === robot_path[j][i][1]
          );
          if (!alreadyInclude) {
            crushPoints.push([robot_path[j][i][0], robot_path[j][i][1]]);
            result++;
          }
        }
      }
    }
  }

  return result;
}