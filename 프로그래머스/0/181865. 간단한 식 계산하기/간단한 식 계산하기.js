function solution(binomial) {
    let [a, op, b] = binomial.split(" ");
    
    switch(op) {
        case '+':
            return (+a) + (+b);
        case '-':
            return (+a) - (+b);
        case '*':
            return (+a) * (+b);
    
    }    
}