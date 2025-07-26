function solution(sequence, k) {
    let answer = [];
    let length = sequence.length;
    
    let left = 0;
    let sum = 0;

    for (let right = 0; right < sequence.length; right++) {
        sum += sequence[right];

        while (sum > k && left <= right) {
            sum -= sequence[left];
            left++;
        }

        if (sum === k) {
            if (right - left < length) {
                length = right - left;
                answer = [left, right];
            }
        }
    }

    return answer;
}