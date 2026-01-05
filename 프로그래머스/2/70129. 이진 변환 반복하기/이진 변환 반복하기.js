function solution(s) {
    let conversionCount = 0;
    let removedZeroCount = 0;

    while (s !== "1") {
        const originalLength = s.length;
        s = s.replace(/0/g, '');
        const newLength = s.length;

        removedZeroCount += (originalLength - newLength);

        s = newLength.toString(2);
        conversionCount++;
    }

    return [conversionCount, removedZeroCount];
}