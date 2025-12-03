function solution(places) {
  const n = 5;
  const answer = [];

  function check(place, startR, startC) {
    const dir = [[1, 0], [0, 1], [-1, 0], [0, -1]];
    const q = [[startR, startC, 0]];
    const visited = Array.from({ length: 5 }, () => Array(5).fill(false));
    visited[startR][startC] = true;
    
    let head = 0;
    while (head < q.length) {
      const [r, c, dist] = q[head++];
      
      if (dist >= 2) continue;

      for (const [dr, dc] of dir) {
        const nr = r + dr;
        const nc = c + dc;

        if (nr < 0 || nr >= n || nc < 0 || nc >= n) continue;
        if (visited[nr][nc]) continue;        
        if (place[nr][nc] === 'X') continue;
        if (place[nr][nc] === 'P') return false;

        visited[nr][nc] = true;
        q.push([nr, nc, dist + 1]);
      }
    }
    return true;
  }

  for (const place of places) {
    let safe = 1;
    
    for (let r = 0; r < n; r++) {
      for (let c = 0; c < n; c++) {
        if (place[r][c] === 'P') {
          if (!check(place, r, c)) {
            safe = 0;
            break; 
          }
        }
      }
      if (safe === 0) break;
    }
    answer.push(safe);
  }

  return answer;
}
