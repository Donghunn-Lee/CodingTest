function solution(maps) {
    const N = maps.length;
    const M = maps[0].length;

    const visited = Array.from({ length: N }, () => Array(M).fill(false));
    const dir = [[0, 1], [1, 0], [0, -1], [-1, 0]];

    const queue = [[0, 0, 1]];
    visited[0][0] = true;

    while (queue.length) {
        const [i, j, dist] = queue.shift();

        if (i === N - 1 && j === M - 1) {
            return dist;
        }

        for (const [di, dj] of dir) {
            const ni = i + di;
            const nj = j + dj;

            if (
                ni >= 0 && ni < N &&
                nj >= 0 && nj < M &&
                !visited[ni][nj] &&
                maps[ni][nj] === 1
            ) {
                visited[ni][nj] = true;
                queue.push([ni, nj, dist + 1]);
            }
        }
    }

    return -1;
}