function solution(diffs, times, limit) {
    let [left, right] = [1, diffs.reduce((a, b) => Math.max(a, b), -Infinity)];

    const checkPossible = (level) => {
        let timeSpent = 0;

        for (let i = 0; i < diffs.length; i++) {
            const diff = diffs[i];
            const timeCur = times[i];
            const timePrev = i === 0 ? 0 : times[i - 1];

            if (diff <= level) {
                timeSpent += timeCur;
            } else {
                const miss = diff - level;
                timeSpent += miss * (timeCur + timePrev) + timeCur;
            }

            if (timeSpent > limit) return false;
        }

        return true;
    };

    while (left < right) {
        const mid = Math.floor((left + right) / 2);

        if (checkPossible(mid)) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }

    return left;
}
