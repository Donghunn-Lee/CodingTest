function solution(distance, rocks, n) {
    let answer = 0;
    let left = 1;
    let right = distance;

    rocks.sort((a, b) => a - b);

    function isValid(d) {
        let removed = 0;
        let prev = 0;

        for (let rock of rocks) {
            if (rock - prev < d) {
                removed++;
            } else {
                prev = rock;
            }
        }

        if (distance - prev < d) {
            removed++;
        }

        return removed <= n;
    }

    while (left <= right) {
        const mid = Math.floor((left + right) / 2);

        if (isValid(mid)) {
            answer = mid;
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return answer;
}