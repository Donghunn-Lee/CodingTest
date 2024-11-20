function solution(price, money, count) {
    let cost = 0;
    let i = 1;
    
    while(i <= count){
        cost += i * price;
        i++;
    }
    
    if (money <= cost) {
        return cost - money;
    }
    
    return 0;
}