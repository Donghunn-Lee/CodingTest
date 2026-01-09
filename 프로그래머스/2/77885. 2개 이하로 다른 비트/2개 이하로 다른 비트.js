function solution(numbers) {
    return numbers.map(number => {
        if (number % 2 === 0) return number + 1;

        let bin = '0' + number.toString(2);
        const idx = bin.lastIndexOf('0');
        
        bin = bin.substring(0, idx) + "10" + bin.substring(idx + 2);
        
        return parseInt(bin, 2);
    });
}