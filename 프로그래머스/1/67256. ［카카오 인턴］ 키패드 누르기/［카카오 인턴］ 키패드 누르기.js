function solution(numbers, hand) {
    let result = '';
    
    const keyMap = {0 : [3, 1]}
    let n = 1;
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            keyMap[n] = [i, j]
            n++;
        }
    }
    
    let leftHand = [3, 0];
    let rightHand = [3, 2];
    const mustLeft = new Set ([1, 4, 7])
    const mustRight = new Set ([3, 6, 9])
    
    const decideHands = (lh, rh, target) => {
        const leftGap = Math.abs(lh[0] - target[0]) + Math.abs(lh[1] - target[1])
        const rightGap = Math.abs(rh[0] - target[0]) + Math.abs(rh[1] - target[1])
        
        if (leftGap < rightGap) {
            return 0;
        } else if (leftGap > rightGap) {
            return 1;
        } else {
            return 2;
        }
    }
    
    numbers.forEach((number, i) => {
        const numPos = keyMap[number];
        
        if (mustLeft.has(number)) {
            leftHand = numPos;
            result += 'L';
            
            return;
        }
        
        if (mustRight.has(number)) {
            rightHand = numPos;
            result += 'R';
            
            return;
        }
        
        const cmd = decideHands(leftHand, rightHand, keyMap[number]);
        
        if (cmd === 0) {
            leftHand = numPos;
            result += 'L'
        } else if (cmd == 1) {
            rightHand = numPos;
            result += 'R'
        } else {
            if (hand === 'left') {
                leftHand = numPos;
                result += 'L'
            } else {
                rightHand = numPos;
                result += 'R'
            }
        }
    })
    
    return result;

}