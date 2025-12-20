function solution(s) {
    if (s.length === 1) return 1;
    let minLength = s.length;

    for (let unit = 1; unit <= Math.floor(s.length / 2); unit++) {
        let compressedStr = "";
        let prev = s.substring(0, unit);
        let count = 1;

        for (let i = unit; i < s.length; i += unit) {
            let curr = s.substring(i, i + unit);

            if (prev === curr) {
                count++;
            } else {
                compressedStr += (count > 1 ? String(count) : "") + prev;
                prev = curr;
                count = 1;
            }
        }

        compressedStr += (count > 1 ? String(count) : "") + prev;

        minLength = Math.min(minLength, compressedStr.length);
    }

    return minLength;
}