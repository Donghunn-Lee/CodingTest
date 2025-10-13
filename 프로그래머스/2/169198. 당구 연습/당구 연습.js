function solution(m, n, startX, startY, balls) {
  const answer = [];

  const dist2 = (x1, y1, x2, y2) => {
    const dx = x1 - x2, dy = y1 - y2;
    return dx * dx + dy * dy;
  };

  for (const [tx, ty] of balls) {
    const candidates = [];

    // 상단 벽 반사: (tx, 2n - ty)
    // 금지: 같은 x에 있고 startY < ty (벽 닿기 전에 타깃을 먼저 맞음)
    if (!(startX === tx && startY < ty)) {
      candidates.push(dist2(startX, startY, tx, 2 * n - ty));
    }

    // 하단 벽 반사: (tx, -ty)
    // 금지: 같은 x에 있고 startY > ty
    if (!(startX === tx && startY > ty)) {
      candidates.push(dist2(startX, startY, tx, -ty));
    }

    // 우측 벽 반사: (2m - tx, ty)
    // 금지: 같은 y에 있고 startX < tx
    if (!(startY === ty && startX < tx)) {
      candidates.push(dist2(startX, startY, 2 * m - tx, ty));
    }

    // 좌측 벽 반사: (-tx, ty)
    // 금지: 같은 y에 있고 startX > tx
    if (!(startY === ty && startX > tx)) {
      candidates.push(dist2(startX, startY, -tx, ty));
    }

    answer.push(Math.min(...candidates));
  }

  return answer;
}